# Lab8_goal_audio_RPI.py
# PV 10/2025

import threading as th
import paho.mqtt.client as mqtt
import sounddevice as sd
import scipy
import time
import json

global broker

#configuration
duration = 3  # seconds
fs = 44100
broker = '192.168.1.98' #MQTT broker

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
        global mqtt_cmd
        print("   --> " + msg.topic+" "+str(msg.payload))
        #print('Message received: ' + str(msg.payload))
        if 'a' in str(msg.payload):
            mqtt_cmd = 'a'
        if 'q' in str(msg.payload):
            mqtt_cmd = 'q'            
            

            
        
    print('Incializing MQTT')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, 1883, 60)
    client.loop_forever()
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
    client = mqtt.Client()
    MQTT_th = th.Thread(target=MQTT_TH, args=[client])
    MQTT_th.start()
    return client




#Main

#Start MQTT connection
client = MQTT_Connect()


#Loop forever
print('Program Ready to receive MQTT commands')
mqtt_cmd=' '
while(True):
    if mqtt_cmd == 'a': 
        print("Recording...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        print("Done.")
        
        # Save locally
        print("saving")
        scipy.io.wavfile.write("output.wav", fs, audio)
        
        # Serialize to json
        print("Serialize")
        audio_json = json.dumps({
            "data": audio.tolist(),
            "dtype": str(audio.dtype),
            "fs": fs
        })
            
        #publish
        client.publish(topic_pub,audio_json)
        print("Image published in MQTT")
        
    if mqtt_cmd == 'q':
        break
    
    mqtt_cmd=' '
    time.sleep(.1)
    

client.disconnect()  #disconnects MQTT  
print("Program Exit") 
