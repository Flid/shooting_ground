import logging

from flask_socketio import emit, join_room, leave_room

from .app import socketio
from .db import ShootingSessionRecord

log = logging.getLogger(__name__)


@socketio.on('message')
def handle_message(message):
    log.info('received message: ' + message)


@socketio.on('connect', namespace='')
def test_connect():
    log.error('New websocket connected')
    join_room('test')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='')
def test_disconnect():
    leave_room('test')
    log.debug('Websocket has been disconnected')


@socketio.on('listening_session', namespace='')
def on_listening_session(data):
    join_room(data['session_id'])
    send_new_data(data['session_id'])


def send_new_data(session_id):
    items = ShootingSessionRecord.query.filter_by(shooting_session_id=session_id).order_by('seconds')
    to_send = []

    for item in items:
        to_send.append(item.payload)

    emit('new_data', to_send)
