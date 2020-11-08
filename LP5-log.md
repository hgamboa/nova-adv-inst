# Lab 5 - Presential - Logging and plotting

## Lab Goals

Save data in a file sampled from an arduino and plot the graph in realtime via a websocket.

## Goal 1 - Setup a server to plot the data in via a web page

We will setup a server on raspberry py to bot serve webpages and send data via a websocket.

A websocket is a comunication protocol enabling fast bidirectional comunication between a server and a/multiple client/s.

This protocol creates a persistent connection, which reduces the time needed to transfer data between two devices. Another advantage of being persistent is the hability of the server to send messages directly to a client (or even multiple) without being "asked", reducing the unwanted traffic in the network and the syncronization of multiple clients.


The first thing to do is run the server. In order to do that, copy the files in the folder ***LP5*** to your raspberry pi, and go to the folder were the server file is and type:

python3 server.py

This will lunch the server. Afterwards, go to a browser (remember that you have to be connected to the "pi" network) and navigate to http://YourRaspberryIp:9999.

You should then see a page (which is inside the static folder called example.html) where you can insert your raspberry's IP and connect to it. If the autofill option is correct, just press the connect button.

If no error alert appears, the web page will start requesting a new sample every seconds and displaying it on the chart.

Both server.py and examples.html files have comments explaing what everything does.



# Goal 2

Now we will modify the server that we configured in Goal 1, to display sensor data aquired from an Android Phone

## Requirements

* From the Play Store, install in a Android Phone, the SensorDroid App
* In your virtual machine:
** Install library: 
**** sudo pip3 install sensordroid
** Download the python Native Example programa SensorDroidNative.py form:
*** https://sites.google.com/view/sensordroid/getting-started/python

## Testing SensorDroid
* On your mobile run the SensorDroid App
** Explore the app the verify which sensors are available in your phone
* In the virtual machine do:
** python3 SensorDroidNative.py
* You should see now a flow of numbers, with the real time data of the phone sensors



Change the code to use the data saved in the file to log from the arduino based on what was done on lab 5.
