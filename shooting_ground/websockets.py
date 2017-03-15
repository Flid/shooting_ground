import logging

from flask_socketio import emit, join_room, leave_room

from .app import socketio
from .db import JobRecord

log = logging.getLogger(__name__)


@socketio.on('message')
def handle_message(message):
    log.info('received message: ' + message)


@socketio.on('connect', namespace='/')
def test_connect():
    log.error('New websocket connected')
    join_room('test')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/')
def test_disconnect():
    leave_room('test')
    log.debug('Websocket has been disconnected')


@socketio.on('listening_job', namespace='/')
def on_listening_job(data):
    join_room('job_' + str(data['job_id']))
    send_new_data(data['job_id'])


def send_new_data(job_id):
    items = JobRecord.query.filter_by(job_id=job_id).order_by('seconds')
    to_send = []

    for item in items:
        to_send.append(item.payload)

    emit('new_data', to_send)
