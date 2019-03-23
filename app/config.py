import os

# obviously not the file used in production
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'XXXXXXXXXXXXXXXXXXXX'
