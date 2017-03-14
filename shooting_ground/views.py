from flask import request
import json
from .app import app
from .db import ShootingSession, ShootingSessionRecord, db
from . import formatters
from .utils import response_ok
from .data_converters import CONVERTERS
from . import forms
from .utils import validate_form
CACHED_PAGES = {}


@app.route('/')
def index():
    #if 'index.html' not in CACHED_PAGES:
    with open('static/index.html') as fd:
        CACHED_PAGES['index.html'] = fd.read()

    return CACHED_PAGES['index.html']


@app.route('/shooting_sessions/', methods=['POST'])
def create_shooting_session():
    form = validate_form(forms.CreateSessionForm)

    ss = ShootingSession(
        name=form.name.data,
    )
    db.session.add(ss)
    db.session.commit()

    return response_ok(formatters.format_shooting_session(ss))


@app.route('/shooting_sessions/', methods=['GET'])
def list_shooting_sessions():
    shooting_sessions = ShootingSession.query.all()

    return response_ok([
        formatters.format_shooting_session(ss) for ss in shooting_sessions
    ])


@app.route('/shooting_sessions/<int:shooting_session_id>/records/', methods=['POST'])
def create_shooting_session_record(shooting_session_id):
    form = validate_form(forms.CreateSessionRecordForm)

    converter = CONVERTERS[form.type.data]

    ssr = ShootingSessionRecord(
        shooting_session_id=shooting_session_id,
        seconds=form.seconds.data,
        payload=json.dumps(converter(form.payload.data)),
    )
    db.session.add(ssr)
    db.session.commit()

    return response_ok(formatters.format_shooting_session_record(ssr))


@app.route('/shooting_sessions/<int:shooting_session_id>/records/', methods=['GET'])
def list_shooting_session_records(shooting_session_id):
    records = ShootingSessionRecord.query.filter_by(
        shooting_session_id=shooting_session_id,
    ).order_by('seconds')
    return response_ok([
        formatters.format_shooting_session_record(r) for r in records
    ])


@app.route('/emit', methods=['GET'])
def emit_socket_message():
    from flask_socketio import emit, join_room, leave_room, send
    emit('test_message', {'a': 'b'}, namespace='', room='test')
    return 'Done'
