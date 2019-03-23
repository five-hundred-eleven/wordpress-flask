from pythonwp import db

class TermTaxonomy(db.Model):

    __tablename__ = "wp_term_taxonomy"

    term_taxonomy_id = db.Column('term_taxonomy_id', db.Integer(), primary_key=True, nullable=False)
    term_id = db.Column('term_id', db.Integer(), primary_key=False, nullable=False)
    taxonomy = db.Column('taxonomy', db.String(length=32), primary_key=False, nullable=False)
    description = db.Column('description', db.Text(length=None), primary_key=False, nullable=False)
    parent = db.Column('parent', db.Integer(), primary_key=False, nullable=False)
    count = db.Column('count', db.Integer(), primary_key=False, nullable=False)
    db.UniqueConstraint('term_id', 'taxonomy')
    db.ForeignKeyConstraint(['term_id'], ['wp_terms.term_id'])
    db.ForeignKeyConstraint(['parent'], ['wp_term_taxonomy.term_taxonomy_id'])
