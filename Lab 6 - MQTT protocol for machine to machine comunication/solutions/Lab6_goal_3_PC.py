# Lab6_goal_3_PC.py
# AAIB 25/26 (PV)

import threading as th
import paho.mqtt.client as mqtt
import time

global topic_sub, topic_pub
global broker


#MQTT Thread Function
def MQTT_TH(client):
    # The callback function for when the client receives a CONNECT response from the server.
    def on_connect(client, userdata, flags, rc):
        print("\tMQTT connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(topic_sub+'/#')
        
    # The callback function for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        #print("   --> " + msg.topic+" "+str(msg.payload))
        print("  --> Reply: " + str(msg.payload))
        
    print('Incializing MQTT')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, 1883, 60)
    client.loop_forever()
    print('MQTT link ended')


#main program

#Set IP of the AAIB lab broker
broker = '192.168.1.98'

#define the topic of publication. the prefix AAI is allways used
topic_prefix = 'AAIB/'
topic = input("topic to be used: ")
topic_sub = topic_prefix + topic +'/data'
topic_pub = topic_prefix + topic +'/cmd'
print('Subscribe topic: ' + topic_sub)
print('Publish topic: ' + topic_pub)

#start thread associated to MPTT listening  
print('\tMQTT starting')
client = mqtt.Client()
MQTT_th = th.Thread(target=MQTT_TH, args=[client])
MQTT_th.start()

#receive messages forever (Ctrl-C to end)
time.sleep(0.5) #0.5s delay to connection be ready
op = 0
while op != 'x' and op != 'X': 
    op = input("Audio N to classity (x to exit): ")
    client.publish(topic_pub, op) 
    time.sleep(0.1)
    if(op == 'x' or op == 'X'):
        break
 
client.disconnect()  #disconnects MQTT  
print("Program Exit")



