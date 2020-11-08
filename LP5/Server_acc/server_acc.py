import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
# The imports above are the function/classes we will need
# to lunch our webserver.
import os
import random
import time

from sensordroid import Client

AccValueData=5

#####################################################
# routines to Sensordroid
def devicesDiscoveredEventHandler(devices):
    print(devices)
    if len(devices) > 0:
        client = Client(devices[0])

        client.connectionUpdated = connectionUpdatedEventHandler
        client.sensorsReceived = sensorsReceivedEventHandler
        client.imageReceived = cameraReceivedEventHandler

        client.sensorsSampleRate = 100
        client.cameraResolution = 13

        client.connect()
        

def connectionUpdatedEventHandler(sender, msg):
    if sender is not None:
        if sender.connected:
            print("Connected")
        else:
            print("Disonnected") 

def sensorsReceivedEventHandler(sender, dataCurrent):
    global AccValueData
    #print(sender.name + ": Acceleration [" + dataCurrent.Acceleration.Values.AsString + "]")
    a=dataCurrent.Acceleration.Values.AsDouble
    #print(a[0])
    AccValueData=a[0]
    print(AccValueData)



def cameraReceivedEventHandler(sender, image):
    #Process image data bytes
    print("New image");
    pass

########################################################
#Routines to server


# This class will be called when you visit or make a GET request
# to http:RASPIP:8888/ and will return the example.html page inside
# the static folder.
class index(tornado.web.RequestHandler):
    def get(self):
        self.render("static/example.html")
# This class is responsible to create a websocket between the client
# and the server, allowing for a persistent connection between them 
# and the hability of sending data in a fast and reliable way.
# To check the connection flow consult lab 9 readme.md file.
class WSHandler(tornado.websocket.WebSocketHandler):
    # This method will be called when a new client connects to the websocket
    def open(self):
        print('New Connection From:'+self.request.remote_ip)
        #print(type(self.request))
        #print(self.request)
        #print(self.request.remote_ip)
    
    # This method will be called when a new message from a client arrive
    def on_message(self, message):
        global AccValueData
        # Messages in websockets are usually passed as a JSON message (In string form).
        # JSON is more a less a dictionary, where you can have multiple
        # of key:values pairs.
        # The following line parses these json messages to python dictionaries
        js = tornado.escape.json_decode(message)

        # This 'type' is define in our html page. 
        if(js['type'] == 'sendData'):
            #self.write_message({'timestamp': time.time(), 'data': random.randint(0,10)})
            self.write_message({'timestamp': time.time(), 'data': AccValueData})
            #print(AccValueData)
# We need to tell our webserver what is the path to the static folder, since the
# html page will need to access files from this folder.
settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}

# Our server needs to know what to do when you navigate to a web address. The next
# function maps a web address to a class. r'/' is connected to index while
# r'/ws' is connected to web socket handler. This is called routing.

application = tornado.web.Application(handlers=[
    (r'/', index),
    (r'/ws', WSHandler)
], **settings)


#Lauch Sensordroid
Client.devicesDiscovered = devicesDiscoveredEventHandler
Client.startDiscovery()

# This will launch our http server on port 9999. To access it
# you need to navigate to http:RASPIP:99990/ and you should see
# the HTML page.

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(9999)
print('System Ready. ^C to kill')
tornado.ioloop.IOLoop.instance().start()

#close ServerDroid
Client.closeAll()
