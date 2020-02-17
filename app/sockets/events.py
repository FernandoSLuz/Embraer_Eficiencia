from .. import socketio
from flask_socketio import emit
import json
from flask import session

@socketio.on('my_broadcast_event')
def test_broadcast_message(message):
    if(isinstance(message, str)):
        message = json.loads(message)
    print("recieved message")
    content = message['content']
    emit_type = message['emit_type']
    emit('my_response', {'emit_type': emit_type, 'content': content}, broadcast=True)