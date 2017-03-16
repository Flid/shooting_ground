import os
import sys


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
DEBUG = os.environ.get('DEBUG', False)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s',
        },
        'standard': {
            'format': ' %(asctime)s %(message)s',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout,
        },
    },

    'loggers': {
        'shooting_ground': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
    },
}


TEMPLATES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../static/templates',
)
