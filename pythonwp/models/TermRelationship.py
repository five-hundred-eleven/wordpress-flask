from pythonwp import db

class TermRelationship(db.Model):

    __tablename__ = "wp_term_relationships"

    object_id = db.Column('object_id', db.Integer(), primary_key=True, nullable=False)
    term_taxonomy_id = db.Column('term_taxonomy_id', db.Integer(), primary_key=True, nullable=False)
    db.ForeignKeyConstraint(['term_taxonomy_id'], ['wp_term_taxonomy.term_taxonomy_id'])
