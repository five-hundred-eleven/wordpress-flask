from pythonwp import app
from flask import abort, jsonify, request
from pythonwp.models.Post import Post

def jsonifyPost(post):
    return {
            'post_id': post.post_id,
            'post_title': post.post_title,
            }

@app.route('/posts', methods=['GET'])
def getAllPosts():
    posts = Post.query.all()
    return jsonify({
        'posts': [jsonifyPost(post) for post in posts]
    })
