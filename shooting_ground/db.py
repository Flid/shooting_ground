import datetime

from flask_sqlalchemy import SQLAlchemy

from .app import app
from .config import SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<%s %s>' % (
            self.__class__.__name__,
            self.name,
        )


class JobRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    job = db.relationship(
        'Job',
        backref=db.backref('records', lazy='dynamic'),
    )
    seconds = db.Column(db.Float)
    payload = db.Column(db.Text)
    raw_payload = db.Column(db.Text)
    source_type = db.Column(db.Text)

    __table_args__ = (
        db.UniqueConstraint('job_id', 'seconds', name='_unique_job_seconds'),
    )

    def __repr__(self):
        return '<%s %s %s>' % (
            self.__class__.__name__,
            self.job_id,
            self.seconds,
        )
