from flask import jsonify, request
from .exceptions import ValidationError


def response_ok(data):
    return jsonify({
        'status': 'ok',
        'data': data,
    })


def validate_form(form_class):
    form = form_class(request.form)

    is_valid = form.validate()

    if not is_valid:
        raise ValidationError(form.errors)

    return form
