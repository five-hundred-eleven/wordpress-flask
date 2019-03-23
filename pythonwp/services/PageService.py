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
