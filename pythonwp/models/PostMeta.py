from pythonwp import db

class PostMeta(db.Model):

    __tablename__ = "wp_postmeta"

    meta_id = db.Column('meta_id', db.Integer(), primary_key=True, nullable=False)
    post_id = db.Column('post_id', db.Integer(), primary_key=False, nullable=False)
    meta_key = db.Column('meta_key', db.String(length=255), primary_key=False)
    meta_value = db.Column('meta_value', db.Text(length=None), primary_key=False)
    db.ForeignKeyConstraint(['post_id'], ['wp_posts.ID'])
