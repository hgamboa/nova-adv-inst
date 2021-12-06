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
        return np.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = "192.168.1.155"
        #host = "10.211.136.20"
        port = 4242
        s.connect((host, port))

        while not thread_stop_event.isSet():
            #time.sleep(0.025)
            data = s.recv(256)
            if data:
                decoded_data = data.decode("utf-8").split("\n")
                for msg in decoded_data:
                    try:
                        package = json.loads(msg)
                        print(package)
                        t=package["accelerometer"]["timestamp"]
                        acc=package["accelerometer"]["value"]
                        a = str(t)+','+str(acc[0])+','+str(acc[1])+','+str(acc[2])
                        print(a)
                        f=open("test2.txt",'a')
                        f.write(a+'\n')
                        f.close()
                        socketio.emit('serverResponse', {'timestamp':t, 'data': acc[0]})

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

