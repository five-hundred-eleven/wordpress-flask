import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "XXXXXXXXXXXXXXXXXXXX"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql:///" + os.path.join(basedir, "app.db")
    #  SQLALCHEMY_DATABASE_URI="mysql://wpuser:9n&Z5sAR7BFn&Chp@localhost/stromsydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
