import time
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('index.html')


@socketio.on('sendData')
def handle_my_custom_event(json):
    emit('serverResponse', {'timestamp': time.time(), 'data': random.randint(0, 10)})


if __name__ == '__main__':
    socketio.run(app, debug=True)