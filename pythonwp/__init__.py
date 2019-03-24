from config import Config
from flask import Flask, session
from flask_session import Session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os, sys

app_base = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_base)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Session(app)

from web import StaticRoutes
from web import PageRoutes
from web import PostRoutes
from web import UserRoutes
