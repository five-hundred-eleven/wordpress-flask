from pythonwp import db

class Link(db.Model):

    __tablename__ = "wp_links"

    link_id = db.Column('link_id', db.Integer(), primary_key=True, nullable=False)
    link_url = db.Column('link_url', db.String(length=255), primary_key=False, nullable=False)
    link_name = db.Column('link_name', db.String(length=255), primary_key=False, nullable=False)
    link_image = db.Column('link_image', db.String(length=255), primary_key=False, nullable=False)
    link_target = db.Column('link_target', db.String(length=25), primary_key=False, nullable=False)
    link_category = db.Column('link_category', db.Integer(), primary_key=False, nullable=False)
    link_description = db.Column('link_description', db.String(length=255), primary_key=False, nullable=False)
    link_visible = db.Column('link_visible', db.String(length=1), primary_key=False, nullable=False)
    link_owner = db.Column('link_owner', db.Integer(), primary_key=False, nullable=False)
    link_rating = db.Column('link_rating', db.Integer(), primary_key=False, nullable=False)
    link_updated = db.Column('link_updated', db.DateTime(timezone=False), primary_key=False, nullable=False)
    link_rel = db.Column('link_rel', db.String(length=255), primary_key=False, nullable=False)
    link_notes = db.Column('link_notes', db.Text(length=None), primary_key=False, nullable=False)
    link_rss = db.Column('link_rss', db.String(length=255), primary_key=False, nullable=False)
    db.ForeignKeyConstraint(['link_owner'], ['wp_users.ID'])

