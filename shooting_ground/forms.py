from wtforms import FloatField, Form, StringField, validators

from .data_converters import CONVERTERS


class CreateJobForm(Form):
    name = StringField('Username', [validators.Length(max=128)])


class CreateJobRecordForm(Form):
    seconds = FloatField(validators=[
        validators.NumberRange(min=0),
    ])
    type = StringField(validators=[
        validators.AnyOf(set(CONVERTERS.keys())),
    ])
    payload = StringField(validators=[
        validators.InputRequired(),
    ])
