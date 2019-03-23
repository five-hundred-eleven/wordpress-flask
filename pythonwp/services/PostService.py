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

    def getAllPosts(self):
        return (
            Post.query
                .filter(Post.post_type=="post")
                .order_by(Post.post_date.desc())
        )

    def getBoundedActivePosts(self, first=0, num=10):
        return (
            self.getActivePosts()
                .offset(first)
                .limit(num)
        )

    def getBoundedAllPosts(self, first=0, num=20):
        return (
            self.getAllPosts()
                .offset(first)
                .limit(num)
        )

    def getPostById(self, post_id):
        return (
            Post.query
                .filter(db.and_(
                    Post.post_type=="post",
                    Post.post_id==post_id
                ))
                .one()
        ) 

    def getPostRevisionsById(self, post_id):

        top_post = self.getPostById(post_id)
        return (
            Post.query
                .filter(db.and_(
                    Post.post_type.in_(("post", "revision")),
                    Post.post_name==top_post.post_name
                ))
        )
