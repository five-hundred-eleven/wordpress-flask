from config import Config
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, sys

app_base = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_base)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from web import StaticRoutes
from web import PageRoutes
from web import PostRoutes
from web import UserRoutes
