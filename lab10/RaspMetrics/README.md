# Python Web Server Example

## Introduction

This script serves as an exemple how to setup a simple web server, in this case a simple REST API using the Tornado framework.

REST is another way to send messages between a web server and a client. In lab 9, there was a brief overview on websockets, and the main difference between these two methods is the how both manage the connection.

Unlike a websocket, a REST connection is close in when the response is passed. This introduces more overhead if you have a real time application, like a web chat or real time data acquisition. 

Nevertheless, REST api's still have a place in the world, since the have a more universal support, scale better (since your server does not have to manage multiple connected clients), and for a one-off request/reponse is very usefull.

## Requirements

For this server the only dependency is the tornado library, which you can install using either 

	sudo pip3 install tornado
	
or

	sudo python3.7 -m pip install tornado
	
depending if you want to use python3.6 (default) or python3.7.

## Project structure and explanation

There are two files, get_stats.py and stats_server.py. 

The get_stats.py is a simple file cointaining the different function to get CPU load, CPU temperature, Memory usage and Uptime. Since we are using a unix base operating system, these metrics can be obtain by simply reading some files.

The stats_server.py file is our web server. This file is also pretty simple, and it has two end points (web address that when we visit the web server responds): /  and /stats. 

This server is lunched in port 8888 and you can access the server by visiting either http:// RASPBERRY IP:8888/ to get an 'Alive' message or visit http:// RASPBERRY IP:8888/stats to get the metrics from get_stats.py file.

Since to measure CPU load you have a small time interval, when you call ttp:// RASPBERRY IP:8888/stats you can also pass an optional ?interval  argument to change this polling interval. P.e, if wanted to wait 0.1 seconds between CPU measurments, you would query the server using ttp:// RASPBERRY IP:8888/stats?interval=0.1.

For more detail, open the python files and read the comments trought out the code and also read the [Tornado user guide](https://www.tornadoweb.org/en/stable/guide.html).