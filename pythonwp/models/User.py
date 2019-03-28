from flask_login import UserMixin
from pythonwp import db, login

class User(UserMixin, db.Model):
    
    __tablename__ = "wp_users"

    user_id = db.Column('ID', db.Integer(), primary_key=True, nullable=False)
    user_login = db.Column('user_login', db.String(length=60), primary_key=False, nullable=False)
    user_pass = db.Column('user_pass', db.String(length=255), primary_key=False, nullable=False)
    user_nicename = db.Column('user_nicename', db.String(length=50), primary_key=False, nullable=False)
    user_email = db.Column('user_email', db.String(length=100), primary_key=False, nullable=False)
    user_url = db.Column('user_url', db.String(length=100), primary_key=False, nullable=False)
    user_registered = db.Column('user_registered', db.DateTime(timezone=False), primary_key=False, nullable=False)
    user_activation_key = db.Column('user_activation_key', db.String(length=255), primary_key=False, nullable=False)
    user_status = db.Column('user_status', db.Integer(), primary_key=False, nullable=False)
    display_name = db.Column('display_name', db.String(length=250), primary_key=False, nullable=False)

    def get_id(self):
        return unicode(self.user_id)

    def serialize(self):

        return {
            'user_id': self.user_id,
            'user_nicename': self.user_nicename,
            'user_email': self.user_email,
            'user_url': self.user_url,
        }

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
