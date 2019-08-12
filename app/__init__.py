from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
# Config
app.config.from_object(config['prod'])
# Addons
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app)

from app import models, routes
