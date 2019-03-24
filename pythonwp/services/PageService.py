from pythonwp.models.Post import Post
from pythonwp import db

class PageService:

    def __init__(self):
        pass

    def getActivePages(self):
        return (
            Post.query
                .filter(db.and_(
                    Post.post_status=="publish",
                    Post.post_type=="page"
                ))
        )

    def getPageById(self, page_id):
        return (
            Post.query
                .filter(db.and_(
                    Post.post_id==page_id,
                    Post.post_type=="page"
                ))
                .one()
        )

    def getPageByName(self, name):
        return (
            Post.query
                .filter(db.and_(
                    Post.post_status=="publish",
                    Post.post_type=="page",
                    Post.post_name==name
                ))
                .one()
        )
