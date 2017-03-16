import json


def format_job(ss):
    return {
        'id': ss.id,
        'name': ss.name,
        'created_at': ss.created_at.isoformat(),
    }


def format_job_record(ssr):
    return {
        'job_id': ssr.job_id,
        'seconds': ssr.seconds,
        'payload': json.loads(ssr.payload),
    }
