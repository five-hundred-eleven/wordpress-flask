from pythonwp.models.Post import Post
from pythonwp import db
from datetime import datetime
import re

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

        revisions = (
            Post.query
                .filter(db.and_(
                    Post.post_type=="revision",
                    Post.post_parent_id==post_id
                ))
        )

        return sorted(revisions, cmp=lambda x, y: -1 if x.post_modified > y.post_modified else 1)

    def updatePostFromJson(self, user, post_id, post_json):

        post = self.getPostById(post_id)
        if post.post_author_id != user.user_id:
            raise AccessDeniedException

        revision = self.__copyPost(Post(), post)
        revision.post_parent_id = post_id
        revision.post_name = str(post.post_id) + "-revision-v1"
        revision.post_type = "revision"

        db.session.add(revision)

        post.post_content = post_json["post_content"]
        post.post_title = post_json["post_title"]
        post.post_modified = datetime.now()
        db.session().commit()

        return post

    def newPostFromJson(self, user, post_json):

        post = Post()
        post.post_title = post_json["post_title"]
        post.post_content = post_json["post_content"]
        post.post_name = re.sub(r"[^a-z ]", "", post.post_title.lower())
        post.post_name = "-".join(post.post_name.split(" "))
        post.post_modified = datetime.now()
        post.post_date = datetime.now()
        post.post_type = "post"
        post.post_author_id = user.user_id
        post.post_status = "publish"

        post = self.__fillPost(post)

        db.session.add(post)
        db.session().commit()

        return post

    def __fillPost(self, post):
        post.post_author_id = post.post_author_id or 0
        post.post_date = post.post_date or datetime.now()
        post.post_date_gmt = post.post_date_gmt or datetime.now()
        post.post_content = post.post_content or ""
        post.post_title = post.post_title or ""
        post.post_excerpt = post.post_excerpt or ""
        post.post_status = post.post_status or ""
        post.comment_status = post.comment_status or ""
        post.ping_status = post.ping_status or ""
        post.post_password = post.post_password or ""
        post.post_name = post.post_name or ""
        post.to_ping = post.to_ping or ""
        post.pinged = post.pinged or ""
        post.post_modified = post.post_modified or datetime.now()
        post.post_modified_gmt = post.post_modified_gmt or datetime.now()
        post.post_content_filtered = post.post_content_filtered or ""
        post.post_parent_id = post.post_parent_id or 0
        post.guid = post.guid or ""
        post.menu_order = post.menu_order or 0
        post.post_type = post.post_type or ""
        post.post_mime_type = post.post_mime_type or ""
        post.comment_count = post.comment_count or 0
        
        return post

    def __copyPost(self, to_post, from_post):
        to_post.post_author_id = from_post.post_author_id or 0
        to_post.post_date = from_post.post_date or datetime.now()
        to_post.post_date_gmt = from_post.post_date_gmt or datetime.now()
        to_post.post_content = from_post.post_content or ""
        to_post.post_title = from_post.post_title or ""
        to_post.post_excerpt = from_post.post_excerpt or ""
        to_post.post_status = from_post.post_status or ""
        to_post.comment_status = from_post.comment_status or ""
        to_post.ping_status = from_post.ping_status or ""
        to_post.post_password = from_post.post_password or ""
        to_post.post_name = from_post.post_name or ""
        to_post.to_ping = from_post.to_ping or ""
        to_post.pinged = from_post.pinged or ""
        to_post.post_modified = from_post.post_modified or datetime.now()
        to_post.post_modified_gmt = from_post.post_modified_gmt or datetime.now()
        to_post.post_content_filtered = from_post.post_content_filtered or ""
        to_post.post_parent_id = from_post.post_parent_id or 0
        to_post.guid = from_post.guid or ""
        to_post.menu_order = from_post.menu_order or 0
        to_post.post_type = from_post.post_type or ""
        to_post.post_mime_type = from_post.post_mime_type or ""
        to_post.comment_count = from_post.comment_count or 0
        
        return to_post
