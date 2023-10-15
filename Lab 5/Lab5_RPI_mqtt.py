# AAI_Lab4_sub.py
# AAI/AAIB 23/24 (PV)


import paho.mqtt.client as mqtt

global topic

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("\tMQTT connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic+'/#')
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("   --> " + msg.topic+" "+str(msg.payload))
    
    #returns message to sender with reply added to topic
    msg_reply='RPI received: '+ str(msg.payload)
    client.publish(topic[:len(topic)-4] + '/reply', msg_reply)


#main program

#define the topic of publication. the prefix AAI is allways used
topic_prefix = 'AAI/'
topic = input("topic to be used: ")
topic = topic_prefix + topic + '/cmd'
print('Full topic subscribed: ' + topic)

#open MQTT connection to broker   
broker = '192.168.1.98' 
print('\tMQTT starting')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)

#receive messages forever (Ctrl-C to end)
print('\nMessages received: ')
client.loop_forever()
print('\tMQTT disconected')



