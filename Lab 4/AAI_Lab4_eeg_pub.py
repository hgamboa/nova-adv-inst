# AAI_Lab4_eeg_pub.py
# AAI/AAIB 23/24 (PV)

import paho.mqtt.client as mqtt
import numpy as np
import json
from time import sleep

broker = '192.168.1.98'

#open MQTT connection to broker
client = mqtt.Client()
client.connect(broker, 1883, 60)

#define the topic of publication. the prefix AAI is allways used
topic_prefix = 'AAI/'
topic = input("topic to be used: ")
topic = topic_prefix + topic
print('Full topic: ' + topic)

# Read ecg file
with open("cleanecg.txt", "r") as fl:
    ecg = fl.readlines()
fl.close()

print('ECG type: ', type(ecg))
print('Lengh of list ECG', len(ecg))
print('Lengh of index[0]', len(ecg[0]))

t = np.array(ecg[0].split()).astype(float).tolist()
s = np.array(ecg[1].split()).astype(float).tolist()

t_len = len(t)
t_1s_len = 100 #100 sample = 1s

for n in range(0,t_len,t_1s_len):
	
	print(n)
	#create ecg list for 1s
	ecg=[[],[]]
	ecg[0]=t[n:(n+t_1s_len)-1]
	ecg[1]=s[n:(n+t_1s_len)-1]

	#publised ecg using json format
	print('publish EEG from', n/t_1s_len, 's to ', (n+1)/t_1s_len, 's')
	client.publish(topic,json.dumps(ecg))

	#sleep for 1s
	sleep(1)

#ends program
client.disconnect()
print("Program Exit")
