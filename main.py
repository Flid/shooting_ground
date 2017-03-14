
from shooting_ground.db import db
from shooting_ground.app import app, init
from shooting_ground.views import *

db.create_all()
init()

