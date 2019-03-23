from pythonwp import db

class UserMeta(db.Model):

    __tablename__ = 'wp_usermeta'

    umeta_id = db.Column('umeta_id', db.Integer(), primary_key=True, nullable=False)
    user_id = db.Column('user_id', db.Integer(), primary_key=False, nullable=False)
    meta_key = db.Column('meta_key', db.String(length=255), primary_key=False)
    meta_value = db.Column('meta_value', db.Text(length=None), primary_key=False)
    db.ForeignKeyConstraint(['user_id'], ['wp_users.ID'])

