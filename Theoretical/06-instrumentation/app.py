import time
import random
import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def sessions():
    package = {"mean": 0, "std": 0}
    return render_template('index.html', result=package)


def process(data):
    features = {"mean": np.mean(data), "std": np.std(data)}

    return features


@socketio.on('sendData')
def handle_my_custom_event(json):
    measure = random.randint(0, 10)
    emit('serverResponse', {'timestamp': time.time(), 'data': measure})
    f = open("data.txt", 'a')
    f.write(str(measure) + '\n')
    f.close()


@socketio.on('process')
def handle_process():
    signal = np.loadtxt("data.txt")
    package = process(signal)
    print(package)

    emit('serverProcessResponse', package)


if __name__ == '__main__':
    socketio.run(app, debug=True)

