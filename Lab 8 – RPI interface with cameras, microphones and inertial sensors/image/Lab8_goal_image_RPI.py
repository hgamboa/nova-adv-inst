# Lab8_goal_image_RPI.py
# PV 10/2025


import cv2
import json
import base64
import numpy as np

import threading as th
import paho.mqtt.client as mqtt

import time

global broker

#configuration

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


#connects to webcam
def WebCam_Connect():
    # Initialize the webcam (usually device 0)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
        
    print("web cam ready")
    return cap



#Main

#Start MQTT connection
client = MQTT_Connect()

#Camera connect
web_cam = WebCam_Connect()


#Loop forever
print('Program Ready to receive MQTT commands')
mqtt_cmd=' '
while(True):
    if mqtt_cmd == 'a': 
        # Read a single frame
        ret, frame = web_cam.read()
        if ret:
            # Save the frame as an image
            cv2.imwrite("webcam_image.jpg", frame)
            print("Image saved as webcam_image.jpg")
            
            #send to mqtt
            # encode to json
            # Encode image as JPEG
            _, frame_64 = cv2.imencode('.jpg', frame)

            # Convert to base64
            image_b64 = base64.b64encode(frame_64).decode('utf-8')

            # Wrap in JSON
            image_json = json.dumps({"image": image_b64})
            
            #publish
            client.publish(topic_pub,image_json)
            print("Image published in MQTT")
        else:
            print("Error: Could not read frame.")
            
    if mqtt_cmd == 'q':
        break
    
    mqtt_cmd=' '
    time.sleep(.1)
    
# Release the webcam
web_cam.release()

client.disconnect()  #disconnects MQTT  
print("Program Exit") 
