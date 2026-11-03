# -*- coding: utf-8 -*-
# Lab6_goal_3_RPI.py
# AAIB 25/26 (PV)

print('Program inicializing. Be pacient.')

# imports
#import Libraries
import numpy as np
from pydub import AudioSegment
import glob
import tsfel
import pickle
import time

import threading as th
import paho.mqtt.client as mqtt

global broker

#configuration
fs=44100                #audio sampling frequency
t=2                     #total time of music sample
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
        global audio_n
        print("   --> " + msg.topic+" "+str(msg.payload))
        #print('Message received: ' + str(msg.payload))
        if msg.payload.isdigit():   #confirm that is a number
            audio_n = int(msg.payload) #nterger of audio track
        else:
            audio_n = -2 #-2 will terminate program
            
        
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

def Model_Load():
    # Load the saved Orange model
    with open('model_audio.pkcls', 'rb') as model_file:
        model = pickle.load(model_file)
        
    # Print or use the model
    print(model)
    return model 


def List_Audio_Files():
    #list all the mp3 in audio_files folder:
    audio_folder = "./audio_files/"
    mp3_files = glob.glob(audio_folder+"*.mp3")
    mp3_files.sort() #by default file list is not sorted.
    
    print('\n'.join('{} -> {}'.format(*k) for k in enumerate(mp3_files)))
    return mp3_files

def Classify(mp3_files, audio_n):
    #extract features
    features=[]     #list of features

    # Load MP3 file
    print('Loading' + mp3_files[int(audio_n)])
    audio = AudioSegment.from_file(mp3_files[int(audio_n)])

    #convert to mono
    audio = audio.set_channels(1)

    # Convert to NumPy array
    signal = np.array(audio.get_array_of_samples())

    #extract part of the signal
    #this is important speedup the process
    n=3
    s=signal[n*fs*t:(n+1)*(fs*t)]

    #extract features
    features.append(tsfel.feature_extraction.features.spectral_centroid(s, fs))
    features.append(tsfel.feature_extraction.features.spectral_decrease(s, fs))
    features.append(tsfel.feature_extraction.features.spectral_kurtosis(s, fs))
    features.append(tsfel.feature_extraction.features.spectral_skewness(s, fs))
    features.append(tsfel.feature_extraction.features.spectral_slope(s, fs))
    features.append(tsfel.feature_extraction.features.spectral_spread(s, fs))
    features.append(tsfel.feature_extraction.features.spectral_variation(s, fs))

    print(features)

    #classification
    prediction = model(features)
    print("Predicted class:", prediction)
    print("Predicted class verbose:", mp3_files[prediction.astype(float).astype(int)])
    return prediction
    

#Main

#Start MQTT connection
client = MQTT_Connect()

#Load Orange model
model = Model_Load()
    
#list mp3 files available
mp3_files = List_Audio_Files()

#Loop forever
print('Program Ready to receive MQTT commands')
audio_n = -1
while(True):
    if(audio_n >= 0 and audio_n < len(mp3_files)):
        c = Classify(mp3_files, audio_n)
        client.publish(topic_pub, 'Prediction = ' + str(c))
        
    if(audio_n >= len(mp3_files) and audio_n >= 0):
        print('ERROR - Audio n file does not exit')
        client.publish(topic_pub, 'ERROR - Audio n file does not exit')
        
    if(audio_n == -2):
        print('Program terminated')
        client.publish(topic_pub, 'Program terminated')
        break
        
    audio_n = -1
    time.sleep(.1)

client.disconnect()  #disconnects MQTT  
print("Program Exit")    
