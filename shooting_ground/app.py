from logging.config import DictConfigurator

from flask import Flask
from flask_socketio import SocketIO

from . import config


app = Flask(__name__, template_folder=config.TEMPLATES_DIR)
socketio = SocketIO(app)


def init():
    from . import views, websockets  # noqa
    DictConfigurator(config.LOGGING).configure()
    socketio.run(app, debug=config.DEBUG, use_reloader=config.DEBUG)
