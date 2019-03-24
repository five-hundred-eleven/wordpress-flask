import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "XXXXXXXXXXXXXXXXXXXX"
    SESSION_TYPE = os.environ.get("SESSION_TYPE") or "filesystem"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
