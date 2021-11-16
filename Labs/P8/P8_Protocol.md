# Lab 8 - Logging and real time plotting

## Lab Goal
Build a web application running in the RPi which receive, save and plot realtime sensor data via a WebSocket.


## Pre Lab requirements
Before the lab you should install the required dependencies: 
* [**Flask**](https://flask.palletsprojects.com/en/2.0.x/)
* [**Flask-SocketIO**](https://flask-socketio.readthedocs.io/en/latest/)

You should also install in an Android phone the [SensorStreamer](https://play.google.com/store/apps/details?id=cz.honzamrazek.sensorstreamer) and [Sensors Multi](https://play.google.com/store/apps/details?id=com.wered.sensorsmultitool) apps.

## Lab Goals
You will set up a server on the RPi to bot serve webpages and send data via a [WebSocket](https://sookocheff.com/post/networking/how-do-websockets-work/). A WebSocket is a communication protocol enabling fast bidirectional communication between a server and a/multiple client/s. This protocol creates a persistent connection, which reduces the time needed to transfer data between two devices. Another advantage of being persistent is the ability of the server to send messages directly to a client (or even multiple) without being "asked", reducing the unwanted traffic in the network and the synchronization of multiple clients.


## Goal 1 - An Hello World intro to Flask (15 min.)
Before delving into the development of the WebSocket server, we will set up a basic Flask web app.

1. Write a minimal application in Flask which prints "Hello, World!" on a static webpage in your laptop.
2. Copy the Flask app files to the RPi and deploy the webpage in the RPi. (When you run server, you will notice that the server is only accessible from the RPi)
3. Make the server publicly available so you can access it with your laptop and/or smartphone.

Hint: Check the official [Flask quickstart documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/) and [The Flask Mega-Tutorial Part I](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).


## Goal 2 - Intro to WebSockets with Flask (30 min.)
Our web app will rely on Socket.io as our WebSocket interface. Socket.IO is a JavaScript library for realtime web applications. It enables realtime, bi-directional communication between web clients and servers.
To use Socket.io in the server-side (RPi) we will use the Flask-SocketIO Python package. In the webpage we will import the Socket.IO JavaScript library in the html code.

1. Write a Flask app that sends random integers being generated at a frequency of 1 Hz and run in your laptop.
   We already provide some starting code available [here](Goal_2/). Study the code and complete the 3 TODOs which are identified 
2. Copy the Flask app to the RPi and deploy the server.
3. Make the server publicly available so you can access it with your laptop and/or smartphone.


## Goal 3 - Real-time Plotting with Chart.js (Random Data) (15 min.)
In this goal, we will implement a real-time visualization of incoming random data. We will use Chart.js, a free, open-source JavaScript library for data visualization. We will periodically request a message and reply with a random integer. When the message is received, we will update in real-time the Chart.js visualization.
This goal is demonstrative. You should take this time to study and understand the provided code thoroughly.

1. Reuse the same `app.py`from the previous goal to emit a message upon request with a random integer.
2. Study the HTML and JavaScript code available in the [here](LP5/Goal_3/templates/index.html)  
3. Copy the Flask app to the RPi and deploy the server.
4. Make the server publicly available so you can access it with your laptop and/or smartphone.


## Goal 4 - Real-time Plotting with Chart.js (Sensor Data) (60 min.)
Now we will modify the server that we have previously configured to display sensor data acquired from an Android phone.
1. Explore the sensors available on your Android phone with the [Sensors Multi](https://play.google.com/store/apps/details?id=com.wered.sensorsmultitool) app. It is suggested that you study the accelerometer in more detail. You can read the [Android developer guide](https://developer.android.com/guide/topics/sensors/sensors_motion#sensors-raw-data) documentation to understand how you can work with accelerometer data.
2. Configure your [SensorStreamer](https://play.google.com/store/apps/details?id=cz.honzamrazek.sensorstreamer) app to stream a JSON packet with Accelerometer data at Medium period (60 ms).
3. Write a Flask app that receives real-time accelerometer data, calculates the magnitude of the acceleration, and retransmits it through a WebSocket, so you can visualize the data in real-time. The data in the smartphone must be acquired every 60 ms. The data must be sampled at 40 Hz.  
   We already provide some starting code available [here](LP5/Goal_4/). Study the code and complete the 3 TODOs which are identified.
   The implementation assumes you will start acquiring the smartphone data with before launching the [SensorStreamer](https://play.google.com/store/apps/details?id=cz.honzamrazek.sensorstreamer) app.
4. Make the server publicly available so you can access it with your laptop and/or smartphone.
5. Change the `app.py` to receive additional sensors and save all the sensor data in a file. You might consider reducing the acquisition sampling rate to reduce the bandwidth.
6. Visualize the data contained in the file after the acquisition. Use the matplotlib plotting functions.
