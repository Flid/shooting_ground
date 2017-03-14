from wtforms import Form, StringField, validators, FloatField
from .data_converters import CONVERTERS

class CreateSessionForm(Form):
    name = StringField('Username', [validators.Length(min=4, max=128)])


class CreateSessionRecordForm(Form):
    seconds = FloatField(validators=[
        validators.NumberRange(min=0),
    ])
    type = StringField(validators=[
        validators.AnyOf(set(CONVERTERS.keys())),
    ])
    payload = StringField(validators=[
        validators.InputRequired(),
    ])
