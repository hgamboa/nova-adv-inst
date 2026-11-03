# -*- coding: utf-8 -*-

# Lab8_goal_imu_RPI.py
# PV 10/2025

import threading as th
import paho.mqtt.client as mqtt
from bleak import BleakScanner, BleakClient
import uuid
import time
import asyncio
import json

#configuration
broker = '192.168.1.98' #MQTT broker

#this is what identifies your M5Stick. Must be personalized
DEVICE_NAME = "M5-STICK-01"
SERVICE_UUID = uuid.UUID("94039c15-338f-4297-9014-aaba7d760713")
CHAR_UUID = uuid.UUID("94039c15-338f-4297-9014-aaba7d760713")

#BLE Thread Function
def BLE_TH():
    global loop    
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    address = loop.run_until_complete(scan_ble())
    print(f"device address: {address}")
    if address != 0:
       print("device found")
       ble_client = loop.run_until_complete(connect_ble(address))
    print("BLE thread ended")

#scan for BLE devices in range
async def scan_ble():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover(timeout=5.0)
    for d in devices:
        print(f"{d.name} - {d.address}")
    device = list(filter(lambda d: d.name == DEVICE_NAME, devices))
    if len(device) == 0:
        #raise RuntimeError(f"Failed to find a device name '{DEVICE_NAME}'")
        print(f"Failed to find a device name '{DEVICE_NAME}'")
        return 0
    else:
        return device[0].address
    print("BLE scan done.")

#connect to the the m5-stick device 
ble_data = []
ble_aq_flag = False
async def connect_ble(address):
        global ble_client
        global stop_event
    
        ble_client = BleakClient(address)
        await ble_client.connect()

        while not ble_client.is_connected:
           print("Trying to reconnect...")
           await asyncio.sleep(2)
           await ble_client.connect()
        print("Connected!")

        #wait for data from device
        print("Waiting data from device")
        value = await ble_client.read_gatt_char(CHAR_UUID)
        print("Read value:", value)

        #send data to device
        print("Sending data to device")
        message = bytearray(b"RPI ready")
        await ble_client.write_gatt_char(CHAR_UUID, message, True)

        #set stop event
        stop_event = asyncio.Event()

        #callback to receive data from device
        def callback(sender, data):
            global ble_data
            global ble_aq_flag
            #print(f"Received: {data}")
            data=str(data, 'utf-8')
            print(data)
            #Start aquisition
                
            if "End" in data or "Stop" in data:
                ble_aq_flag = False
                
            if ble_aq_flag == True:
                ble_data.append(data)
                
            if "Start" in data:
                ble_data = []
                ble_aq_flag = True
                
            if ble_aq_flag == False and len(ble_data) != 0:
                #publish data
                MQTT_client.publish(topic_pub, json.dumps(ble_data))
                #save in file
                with open('imu_data.csv', 'w') as f:
                    f.write('\n'.join(ble_data))
                ble_data = []
                
        print("Subscribing to characteristic changes...")
        await ble_client.start_notify(CHAR_UUID, callback)
        
        # Block forever (or until you set the event)
        #stop_event = asyncio.Event()
        await stop_event.wait()
        await ble_client.disconnect()
        print("BLE disconnected")


def send_msg_ble(msg):
    async def send():
        await ble_client.write_gatt_char(CHAR_UUID, msg, response=True)
        print("Sent:", msg)

    future = asyncio.run_coroutine_threadsafe(send(), loop)
    try:
        future.result(timeout=2)  # Optional: wait for completion
    except Exception as e:
        print("Send failed:", e)
        
 
        
#MQTT Thread Function
def MQTT_TH(MQTT_client):
    # The callback function for when the MQTT_client receives a CONNECT response from the server.
    def on_connect(MQTT_client, userdata, flags, rc):
        print("\tMQTT connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        MQTT_client.subscribe(topic_sub+'/#')
        
    # The callback function for when a PUBLISH message is received from the server.
    def on_message(MQTT_client, userdata, msg):
        global mqtt_cmd
        print("   --> " + msg.topic+" "+str(msg.payload))
        #print('Message received: ' + str(msg.payload))
        if 'a' in str(msg.payload):
            mqtt_cmd = 'a'
        if 'q' in str(msg.payload):
            mqtt_cmd = 'q'     
        if 's' in str(msg.payload):
            mqtt_cmd = 's' 
                    
    print('Incializing MQTT')
    MQTT_client.on_connect = on_connect
    MQTT_client.on_message = on_message
    MQTT_client.connect(broker, 1883, 60)
    MQTT_client.loop_forever()
    print('MQTT link ended') 

        
def MQTT_Connect():
    global topic_sub
    global topic_pub
    #define the topic of publication. the prefix AAI is allways used
    topic_prefix = 'AAIB/'
    topic = input("topic to be used: ")
    topic_sub = topic_prefix + topic +'/cmd'
    topic_pub = topic_prefix + topic +'/data'
    print('Subscribe topic: ' + topic_sub)
    print('Publish topic: ' + topic_pub)

    #start thread associated to MPTT listening  
    print('\tMQTT starting')
    MQTT_client = mqtt.Client()
    MQTT_th = th.Thread(target=MQTT_TH, args=[MQTT_client])
    MQTT_th.start()
    return MQTT_client

# main()

#Start MQTT connection
MQTT_client = MQTT_Connect()

#start BLE Thread
BLE_th = th.Thread(target=BLE_TH)
BLE_th.start()

print('Program Ready to receive MQTT commands')
mqtt_cmd=' '
while(True):
    if mqtt_cmd == 'a': 
        print("Start Aquiring data...")
        #example to start 100 aquisitions with a sample rate 50 samples/s
        send_msg_ble(b"start,100,50")
    if mqtt_cmd == 's': 
        print("Aquisition stoped.")
        #example to start 100 aquisitions with a sample rate 50 samples/s
        send_msg_ble(b"stop")
    if mqtt_cmd == 'q': 
        stop_event.set()
        time.sleep(5)
        break
    
    mqtt_cmd=' '
    time.sleep(.1)
  
MQTT_client.disconnect()  #disconnects MQTT  
print("Program Exit") 
    
    #cmd = input("Send message or 'stop': ")
    #if cmd == "stop":
    #  send_msg_ble(b"disconnecting")
    
    #  stop_event.set()
    #  break
    #send_msg_ble(b"start,100,99")
    




