from pythonwp import db

class Option(db.Model):

    __tablename__ = "wp_options"

    option_id = db.Column('option_id', db.Integer(), primary_key=True, nullable=False)
    blog_id = db.Column('blog_id', db.Integer(), primary_key=True, nullable=False)
    option_name = db.Column('option_name', db.String(length=64), primary_key=True, nullable=False)
    option_value = db.Column('option_value', db.Text(length=None), primary_key=False, nullable=False)
    autoload = db.Column('autoload', db.String(length=3), primary_key=False, nullable=False)
