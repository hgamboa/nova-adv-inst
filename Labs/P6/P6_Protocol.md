# Lab 5 - Building a Flask Web Application

## Lab Goal

Build a web application running in the RPi which receive, save and plot realtime sensor data via a WebSocket.

## Pre Lab requirements

Before the lab you should install the required dependencies: 

* [**Flask**](https://flask.palletsprojects.com/en/2.0.x/)
  * `sudo pip3 install Flask`
  * `sudo pip3 install Flask --update`
* [**Flask-SocketIO**](https://flask-socketio.readthedocs.io/en/latest/)
  * `sudo pip3 install flask-socketio`

**Note:** If during the executions of your programs, jinja2 library is not found, install it by:

-  `sudo pip3 install jinja2`

## Lab Goals

You will set up a server on the RPi to bot serve webpages and send data via a [WebSocket](https://sookocheff.com/post/networking/how-do-websockets-work/). A WebSocket is a communication protocol enabling fast bidirectional communication between a server and a/multiple client/s. This protocol creates a persistent connection, which reduces the time needed to transfer data between two devices. Another advantage of being persistent is the ability of the server to send messages directly to a client (or even multiple) without being "asked", reducing the unwanted traffic in the network and the synchronization of multiple clients.

## Goal 1 - An Hello World intro to Flask (15 min.)

Before developing into the development of the WebSocket server, we will set up a basic Flask web app.

1. Write a minimal application in Flask which prints "Hello, World!" on a static webpage. Use nano editor to do it. See following link:
   1. [Quickstart &#8212; Flask Documentation (2.0.x)](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application)
2. Make the server publicly available so you can access it with your laptop and/or smartphone, run the following commands in the command prompt of the RPI
   1. export FLASK_APP=*(your program name)*
   2. flask run --host=*(the IP of your RPI)*
3. At this point, flask web server should have generated a link that you can use in the browser of your computer

**Hint:** For further information see: [Flask quickstart documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/) and [The Flask Mega-Tutorial Part I](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Goal 2 - Intro to the html page (15 min.)

If we intend to do a rich web interface, we must be able to built our own html code and make flask to render them. To do that:

- make a new folder with the name 'templates'

- create your own html file (ex: index.html). If you need inspiration to do that, go to:
  
  - [HTML Tutorial](https://www.w3schools.com/html/default.asp)

- Edit now you your python program from goal 1 and change it to:
  
  - ``from flask import Flask, render_template
    app = Flask(__name__)
    @app.route("/")
    def hello_world():
        return render_template('index.html')``

- Run your new program and see the result in the browser of you computer

- Take a little time in doing a more elaborate html and see the result 

- further information in: [Quickstart &#8212; Flask Documentation (2.0.x)](https://flask.palletsprojects.com/en/2.0.x/quickstart/#)
  
  

## Goal 3 - Intro to WebSockets with Flask (30 min.)

In our applications frequently is necessary to exchange data in real time, between the python program the web page. To do that we will rely on Socket.io as our WebSocket interface. Socket.IO is a JavaScript library f. It enables realtime, bi-directional communication between web clients and servers.
To use Socket.io in the server-side (RPi) we will use the Flask-SocketIO Python package. In the webpage we will import the Socket.IO JavaScript library in the html code.

1. You can find a starting code in (https://github.com/hgamboa/nova-adv-inst/tree/master/Labs/P6/Starting%20code/EX_1). This code show out to stablish a socket link bewteen the python code and the web page, and how to send a randam number every second. Study this code carefully to understand its function blocks
2. Change the code to send a list to 5 random numbers every second and display then in web page
3. change the code to send a string of text, every 2 sec, and display them in the web page 
4. I all the previous situation the request of data by the web page is made periodically. change the program so the request is made only on a button is pressed.
5. To all the exercises, make the server publicly available so you can access it with your laptop and/or smartphone.

## Goal 4 - Real-time Plotting with Chart.js (Random Data) (15 min.)

In this goal, we will implement a real-time visualization of incoming random data. We will use Chart.js, a free, open-source JavaScript library for data visualization. We will periodically request a message and reply with a random integer. When the message is received, we will update in real-time the Chart.js visualization.
This goal is demonstrative. You should take this time to study and understand the provided code thoroughly.

1. Reuse the same `app.py`from the previous goal to emit a message upon request with a random integer.
2. Study the HTML and JavaScript code available in the (https://github.com/hgamboa/nova-adv-inst/tree/master/Labs/P6/Starting%20code/EX_2) 
3. Copy the Flask app to the RPi and deploy the server.
4. Make the server publicly available so you can access it with your laptop and/or smartphone.

## Goal 5 - Real-time Plotting with Chart.js (Sensor Data) (60 min.)

Now we will modify the server that we have previously configured to display sensor data acquired from an Arduino.

1. We are going simulate the sensor data by using the signal generator, connected to one of the analog ports of the Arduino. The signal generated must be at all time between 0 V and 5 V
2. Modify the python program of goal 4, to read the data from Arduino, and save it in a file
3. On the request of the web page, send the data already acquired and display it in the chart. In order to have a realtime representation of the acquired signal, do that request automatically, every second.
4. Make the server publicly available so you can access it with your laptop and/or smartphone.
