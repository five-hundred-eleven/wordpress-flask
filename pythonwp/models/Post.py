from pythonwp import db

class Post(db.Model):
    
    __tablename__ = "wp_posts"

    post_id = db.Column('ID', db.Integer(), primary_key=True, nullable=False)
    post_author = db.Column('post_author', db.Integer(), primary_key=False, nullable=False)
    post_date = db.Column('post_date', db.DateTime(timezone=False), primary_key=False, nullable=False)
    post_date_gmt = db.Column('post_date_gmt', db.DateTime(timezone=False), primary_key=False, nullable=False)
    post_content = db.Column('post_content', db.Text(length=None), primary_key=False, nullable=False)
    post_title = db.Column('post_title', db.Text(length=None), primary_key=False, nullable=False)
    post_excerpt = db.Column('post_excerpt', db.Text(length=None), primary_key=False, nullable=False)
    post_status = db.Column('post_status', db.String(length=20), primary_key=False, nullable=False)
    comment_status = db.Column('comment_status', db.String(length=20), primary_key=False, nullable=False)
    ping_status = db.Column('ping_status', db.String(length=6), primary_key=False, nullable=False)
    post_password = db.Column('post_password', db.String(length=255), primary_key=False, nullable=False)
    post_name = db.Column('post_name', db.String(length=200), primary_key=False, nullable=False)
    to_ping = db.Column('to_ping', db.Text(length=None), primary_key=False, nullable=False)
    pinged = db.Column('pinged', db.Text(length=None), primary_key=False, nullable=False)
    post_modified = db.Column('post_modified', db.DateTime(timezone=False), primary_key=False, nullable=False)
    post_modified_gmt = db.Column('post_modified_gmt', db.DateTime(timezone=False), primary_key=False, nullable=False)
    post_content_filtered = db.Column('post_content_filtered', db.Text(length=None), primary_key=False, nullable=False)
    post_parent = db.Column('post_parent', db.Integer(), primary_key=False, nullable=False)
    guid = db.Column('guid', db.String(length=255), primary_key=False, nullable=False)
    menu_order = db.Column('menu_order', db.Integer(), primary_key=False, nullable=False)
    post_type = db.Column('post_type', db.String(length=20), primary_key=False, nullable=False)
    post_mime_type = db.Column('post_mime_type', db.String(length=100), primary_key=False, nullable=False)
    comment_count = db.Column('comment_count', db.Integer(), primary_key=False, nullable=False)
    fk_post_author = db.ForeignKeyConstraint(['post_author'], ['wp_users.ID'])
    fk_post_parent = db.ForeignKeyConstraint(['post_parent'], ['wp_posts.ID'])
