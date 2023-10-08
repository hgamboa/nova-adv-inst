# AAI_Lab4_pub.py
# AAI/AAIB 23/24 (PV)

import paho.mqtt.client as mqtt

broker = '192.168.1.98'

#open MQTT connection to broker
client = mqtt.Client()
client.connect(broker, 1883, 60)

#define the topic of publication. the prefix AAI is allways used
topic_prefix = 'AAI/'
topic = input("topic to be used: ")
topic = topic_prefix + topic
print('Full topic: ' + topic)

#publised chosen msg
rept = 'y'
while rept != 'n' and rept != 'N': 
	msg = input("message to be published: ")
	client.publish(topic, msg) 
	rept = input("send another message (y/n): ")

#ends program
client.disconnect()
print("Program Exit")
