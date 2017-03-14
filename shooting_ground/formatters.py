import json


def format_shooting_session(ss):
    return {
        'id': ss.id,
        'name': ss.name,
        'created_at': ss.created_at,
    }


def format_shooting_session_record(ssr):
    return {
        'shooting_session': ssr.shooting_session_id,
        'seconds': ssr.seconds,
        'payload': json.loads(ssr.payload),
    }
