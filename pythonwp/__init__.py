from config import Config
from flask import Flask
import os, sys

app_base = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_base)

app = Flask(__name__)
app.config.from_object(Config)
from web import Routes
