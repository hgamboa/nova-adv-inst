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
    # TODO: Emit a dictionary with the current timestamp and a random integer with the following schema:
    # {'timestamp:': #your_code_here, 'data:': #your_code_here}
    # Check on the index.html which event you will need to emit
    # Hint: https://flask-socketio.readthedocs.io/en/latest/api.html#flask_socketio.SocketIO.emit


if __name__ == '__main__':
    socketio.run(app, debug=True)