# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:16:49 2023

@author: pedro
"""

import streamlit as st

from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx
import threading as th
import paho.mqtt.client as mqtt

from streamlit_autorefresh import st_autorefresh


st_autorefresh(interval=1000, key="fizzbuzzcounter")

#MQTT Thread Function
def MQTT_TH(client):

    #MQTT
    # The callback for when the client receives a CONNACK response from the server.
    # for teste: mosquitto_pub -h test.mosquitto.org  -m "celta.jpg" -t "PV/Lactogal/ImgFileName"
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(st.session_state['MyData']['TopicSub'])
    
    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        #store topic and message in session state
        st.session_state['MyData']['Topic'] = msg.topic
        st.session_state['MyData']['Message'] = str(msg.payload)
          
             
   
    print('Incializing MQTT')
    client.on_connect = on_connect
    client.on_message = on_message
    st.session_state['MyData']['Run'] = True
    client.connect(st.session_state['MyData']['Broker'], 1883, 60)
    client.loop_forever()
    print('MQTT link ended')
    st.session_state['MyData']['Run'] = False


#stores states of variables between page refresh
#data that the progrma uses
if 'MyData' not in st.session_state:
    st.session_state['MyData'] = {'Run': False, 'Broker':'192.168.1.98', 'TopicSub':'AAI/#',
                                  'Topic':'', 'Message':''}
    
#mqtt session information
if 'mqttThread' not in st.session_state:
    #open client MQTT connection in an independent thread
    print('session state')
    st.session_state.mqttClient = mqtt.Client()
    st.session_state.mqttThread = th.Thread(target=MQTT_TH, args=[st.session_state.mqttClient]) 
    #st.session_state.mqttThread = th.Thread(target=MQTT_TH, args=[])
    add_script_run_ctx(st.session_state.mqttThread) 
    #st.session_state.mqttThread.start()


#### Page design starts here
st.title("MQTT Comunication")

#MQTT configuration
st.session_state['MyData']['Broker'] = st.text_input('MQTT Broker: ', value='192.168.1.98')
st.session_state['MyData']['TopicSub'] = st.text_input('Topic subscribed: ', value='AAI/PV/reply')

if st.session_state['MyData']['Run']:
    if st.button('MQTT disconnect'):
        st.session_state.mqttClient.disconnect()
else:
    if st.button('MQTT connect'):
        st.session_state.mqttThread.start() #starts thread that controls MQTT
    

#display messages received in subscribed topic
st.header("Messages Received")
st.text('Topic: ' + st.session_state['MyData']['Topic'])
st.text('Message: ' + st.session_state['MyData']['Message'])

#Messages to be published.
st.header("Messages to Transmit")
topic = st.text_input('Topic: ', value='AAI/PV/cmd')
msg = st.text_input('Message: ', value='Hello World')

if st.button('Publish'):
    st.session_state.mqttClient.publish(topic, msg)



