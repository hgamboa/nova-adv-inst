import time
import json
import socket
import numpy as np

from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread, Event

app = Flask(__name__)
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()


def event_stream():

    def get_magnitude(v):
        # TODO: Calculate the magnitude of the acceleration vector. Return must be float.
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #TODO: Define the host and port of the smartphone server
        host =
        port =
        s.connect((host, port))

        while not thread_stop_event.isSet():
            # TODO: Use time.sleep to define a sampling rate of 40 Hz
            # time.sleep()
            data = s.recv(256)
            if data:
                decoded_data = data.decode("utf-8").split("\n")
                for msg in decoded_data:
                    try:
                        package = json.loads(msg)
                        socketio.emit('serverResponse', {'timestamp': time.time(), 'data': get_magnitude(package["accelerometer"]["value"])})

                    except:
                        continue


@app.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('sendData')
def handle_my_custom_event(json):
    global thread
    print('Client connected')

    # Start the thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(event_stream)


if __name__ == '__main__':
    socketio.run(app, debug=True)
