from pythonwp.models.Post import Post
from pythonwp import db

class PostService:

    def __init__(self):
        pass

    def getActivePosts(self):
        return (
            Post.query
                .filter(db.and_(
                    Post.post_status=="publish",
                    Post.post_type=="post"
                ))
                .order_by(Post.post_date.desc())
        )

    def getBoundedActivePosts(self, first=0, num=10):
        return (
            self.getActivePosts()
                .offset(first)
                .limit(num)
        )

