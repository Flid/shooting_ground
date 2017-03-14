from flask_socketio import emit, join_room, leave_room, send
from .app import socketio
import logging

log = logging.getLogger(__name__)


@socketio.on('message')
def handle_message(message):
    log.info('received message: ' + message)


@socketio.on('connect', namespace='')
def test_connect():
    log.debug('New websocket connected')
    join_room('test')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='')
def test_disconnect():
    leave_room('test')
    log.debug('Websocket has been disconnected')

