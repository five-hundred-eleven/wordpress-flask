import os

# obviously not the file used in production
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'WQ3Q5lD6msa8TzZYgWyA'
