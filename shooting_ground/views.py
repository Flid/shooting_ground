import json

from flask.templating import render_template
from flask_socketio import emit

from . import formatters, forms
from .app import app
from .data_converters import CONVERTERS
from .db import Job, JobRecord, db
from .utils import response_ok, validate_form

CACHED_PAGES = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobs/<int:job_id>')
def job_page(job_id):
    return render_template('job.html', job_id=job_id)


@app.route('/jobs/', methods=['POST'])
def create_job():
    form = validate_form(forms.CreateJobForm)

    ss = Job(
        name=form.name.data,
    )
    db.session.add(ss)
    db.session.commit()

    emit(
        'new_jobs',
        {
            'initial': False,
            'items': [formatters.format_job(ss)],
        },
        room='lobby',
        namespace='/',
        broadcast=True,
    )

    return response_ok(formatters.format_job(ss))


@app.route('/jobs/', methods=['GET'])
def list_jobs():
    jobs = Job.query.all()

    return response_ok([
        formatters.format_job(ss) for ss in jobs
    ])


@app.route('/jobs/<int:job_id>/records/', methods=['POST'])
def create_job_record(job_id):
    from flask import request
    form = validate_form(forms.CreateJobRecordForm)

    converter = CONVERTERS[form.type.data]
    payload = converter(form.payload.data)
    payload['seconds'] = form.seconds.data
    payload_str = json.dumps(payload)

    ssr = JobRecord(
        job_id=job_id,
        seconds=form.seconds.data,
        payload=payload_str,
        raw_payload=form.payload.data,
        source_type=form.type.data,
    )
    db.session.add(ssr)
    db.session.commit()

    emit(
        'new_data',
        [payload_str],
        room='job_%s' % job_id,
        namespace='/',
        broadcast=True,
    )

    return response_ok(formatters.format_job_record(ssr))


@app.route('/jobs/<int:job_id>/records/', methods=['GET'])
def list_job_records(job_id):
    records = JobRecord.query.filter_by(job_id=job_id).order_by('seconds')

    return response_ok([
        formatters.format_job_record(r) for r in records
    ])
