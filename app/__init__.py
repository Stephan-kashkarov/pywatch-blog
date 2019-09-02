from flask import Flask
from config import config
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
# Config
app.config.from_object(config['dev'])
# Addons
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app)
login = LoginManager(app)
md = Markdown(app, extensions=['fenced_code'])

from app import models, routes
