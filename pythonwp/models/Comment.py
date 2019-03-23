from pythonwp import db

class Comment(db.Model):

    __tablename__ = "wp_comments"

    comment_ID = db.Column('comment_ID', db.Integer(), primary_key=True, nullable=False)
    comment_post_ID = db.Column('comment_post_ID', db.Integer(), primary_key=False, nullable=False)
    comment_author = db.Column('comment_author', db.Text(length=None), primary_key=False, nullable=False)
    comment_author_email = db.Column('comment_author_email', db.String(length=100), primary_key=False, nullable=False)
    comment_author_url = db.Column('comment_author_url', db.String(length=200), primary_key=False, nullable=False)
    comment_author_IP = db.Column('comment_author_IP', db.String(length=100), primary_key=False, nullable=False)
    comment_date = db.Column('comment_date', db.DateTime(timezone=False), primary_key=False, nullable=False)
    comment_date_gmt = db.Column('comment_date_gmt', db.DateTime(timezone=False), primary_key=False, nullable=False)
    comment_content = db.Column('comment_content', db.Text(length=None), primary_key=False, nullable=False)
    comment_karma = db.Column('comment_karma', db.Integer(), primary_key=False, nullable=False)
    comment_approved = db.Column('comment_approved', db.String(length=4), primary_key=False, nullable=False)
    comment_agent = db.Column('comment_agent', db.String(length=255), primary_key=False, nullable=False)
    comment_type = db.Column('comment_type', db.String(length=20), primary_key=False, nullable=False)
    comment_parent = db.Column('comment_parent', db.Integer(), primary_key=False, nullable=False)
    user_id = db.Column('user_id', db.Integer(), primary_key=False, nullable=False)
    db.ForeignKeyConstraint(['comment_post_ID'], ['wp_posts.ID'])
    db.ForeignKeyConstraint(['comment_parent'], ['wp_comments.comment_ID'])
    db.ForeignKeyConstraint(['user_id'], ['wp_users.ID'])
