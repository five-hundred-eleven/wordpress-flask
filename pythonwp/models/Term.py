from pythonwp import db

class Term(db.Model):

    __tablename__ = "wp_terms"

    term_id = db.Column('term_id', db.Integer(), primary_key=True, nullable=False)
    name = db.Column('name', db.String(length=55), primary_key=False, nullable=False)
    slug = db.Column('slug', db.String(length=200), primary_key=False, nullable=False)
    term_group = db.Column('term_group', db.Integer(), primary_key=False, nullable=False)
    db.UniqueConstraint('slug')
