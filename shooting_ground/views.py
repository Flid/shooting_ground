import json

from . import formatters, forms
from .app import app
from .data_converters import CONVERTERS
from .db import Job, JobRecord, db
from .utils import response_ok, validate_form

CACHED_PAGES = {}


@app.route('/')
def index():
    #  if 'index.html' not in CACHED_PAGES:
    with open('static/index.html') as fd:
        CACHED_PAGES['index.html'] = fd.read()

    return CACHED_PAGES['index.html']


@app.route('/jobs/', methods=['POST'])
def create_job():
    form = validate_form(forms.CreateJobForm)

    ss = Job(
        name=form.name.data,
    )
    db.session.add(ss)
    db.session.commit()

    return response_ok(formatters.format_job(ss))


@app.route('/jobs/', methods=['GET'])
def list_jobs():
    jobs = Job.query.all()

    return response_ok([
        formatters.format_job(ss) for ss in jobs
    ])


@app.route('/jobs/<int:job_id>/records/', methods=['POST'])
def create_job_record(job_id):
    form = validate_form(forms.CreateJobRecordForm)

    converter = CONVERTERS[form.type.data]
    payload = converter(form.payload.data, form.seconds.data)
    payload['seconds'] = form.seconds.data

    ssr = JobRecord(
        job_id=job_id,
        seconds=form.seconds.data,
        payload=json.dumps(payload),
        raw_payload=form.payload.data,
        source_type=form.type.data,
    )
    db.session.add(ssr)
    db.session.commit()

    return response_ok(formatters.format_job_record(ssr))


@app.route('/jobs/<int:job_id>/records/', methods=['GET'])
def list_job_records(job_id):
    records = JobRecord.query.filter_by(job_id=job_id).order_by('seconds')

    return response_ok([
        formatters.format_job_record(r) for r in records
    ])


@app.route('/emit', methods=['GET'])
def emit_socket_message():
    from flask_socketio import emit
    from flask_socketio.namespace import Namespace

    items = JobRecord.query.filter_by(job_id=3).order_by('seconds')
    to_send = []

    for item in items:
        to_send.append(item.payload)

    emit('new_data', to_send, room='job_3', namespace='/', broadcast=True)
    return 'Done'
