# -*- coding: utf-8 -*-
# Lab8_goal_image_PC.py
# PV 10/2025

import streamlit as st

#from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx
from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading as th
import paho.mqtt.client as mqtt
import time
import matplotlib.pyplot as plt
import json
import cv2
import base64
import numpy as np


#MQTT Thread Function
def MQTT_TH(client):

    #MQTT
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(st.session_state['MyData']['TopicSub'])
        st.session_state['MyData']['MQTT_connected'] = True
        st.session_state['MyData']['MQTT_update'] = True
    
    #callback when the client receives disconnect
    def on_disconnect(client, userdata, rc):
        print("Disconnected with result code "+str(rc))
        st.session_state['MyData']['MQTT_connected'] = False
        st.session_state['MyData']['MQTT_update'] = True
    
    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic)
        #store topic and message in session state
        st.session_state['MyData']['Topic'] = msg.topic
        st.session_state['MyData']['Message'] = msg.payload.decode()  # decode once here
        st.session_state['MyData']['MQTT_update'] = True

    print('Image Data Acquisition')
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(st.session_state['MyData']['Broker'], 1883, 60)
    client.loop_forever()
    print('MQTT link ended')



#stores states of variables between page refresh
#data that the progrma uses
#st.session_state works as an global variable
if 'MyData' not in st.session_state:
    st.session_state['MyData'] = {'MQTT_connected': False,'MQTT_update': False, 'Broker':'192.168.1.98', 'TopicSub':'AAI/#',
                                  'Topic':'', 'Message':''}
    
#mqtt thread started
if 'mqttThread' not in st.session_state:
    #open client MQTT connection in an independent thread
    print('session state')
    st.session_state.mqttClient = mqtt.Client()
    st.session_state.mqttThread = th.Thread(target=MQTT_TH, args=[st.session_state.mqttClient]) 
    add_script_run_ctx(st.session_state.mqttThread) 

#### Page design starts here
st.title("Image Acquisition")

#MQTT configuration
st.session_state['MyData']['Broker'] = st.text_input('MQTT Broker: ', value='192.168.1.98')
st.session_state['MyData']['TopicSub'] = st.text_input('Topic subscribed: ', value='AAIB/PV/data')

#MQTT button to connect/disconnect
if st.session_state['MyData']['MQTT_connected']:    
    if st.button('MQTT disconnect'):
        st.session_state.mqttClient.disconnect()
else:
    if st.button('MQTT connect'):
        st.session_state.mqttThread.start() #starts thread that controls MQTT
    

#Messages to be published.
st.header("Messages to Transmit")
topic = st.text_input('Topic: ', value='AAIB/PV/cmd')

if st.button('Request Single Frame'):
    st.session_state.mqttClient.publish(topic, 'a')

if st.button('Terminate RPI Process'):
    st.session_state.mqttClient.publish(topic, 'q')

#display messages received in subscribed topic
st.header("Messages Received")
st.text('Topic: ' + st.session_state['MyData']['Topic'])
#st.text('Message: ' + st.session_state['MyData']['Message'])

#display image
if len(st.session_state['MyData']['Message']) > 0:
   
    #decode from JSON
    # Step 1: Parse JSON
    data=json.loads(st.session_state['MyData']['Message'])
    
    # Step 2: Decode base64 string to bytes
    image_bytes = base64.b64decode(data["image"])
    
    # Step 3: Convert bytes to NumPy array
    np_array = np.frombuffer(image_bytes, dtype=np.uint8)
    
    # Step 4: Decode image using OpenCV
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Step 5: Save image to file (optional)
    cv2.imwrite("webcam_image.jpg", image)
    
    # Step6: Display image
    st.image(image)


#loop waiting for MQTT activity. refresh page when happens    
while True:        
    if st.session_state['MyData']['MQTT_update'] == True:
        st.session_state['MyData']['MQTT_update'] = False
        st.rerun()
        
    time.sleep(.2)

    



