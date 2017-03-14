import json

from shooting_ground.data_converters import CONVERTERS
from shooting_ground.db import ShootingSessionRecord, db


def main():
    for item in ShootingSessionRecord.query.all():
        converter = CONVERTERS[item.source_type]
        payload = converter(item.raw_payload)
        payload['seconds'] = item.seconds
        ShootingSessionRecord.query.filter_by(id=item.id).update({
            'payload': json.dumps(payload),
        })

    db.session.commit()


if __name__ == '__main__':
    main()
