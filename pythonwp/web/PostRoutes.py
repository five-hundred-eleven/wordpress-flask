from pythonwp import app
from flask import abort, jsonify, request
from pythonwp.models.Post import Post
from pythonwp.services import post_service

@app.route('/posts', methods=['GET'])
def getAllPosts():

    first = 0
    if "first" in request.args:
        first = int(request.args.get("first"))
        assert first >= 0

    num = 10
    if "num" in request.args:
        num = int(request.args.get("num"))
        assert first >= 0

    posts = post_service.getBoundedActivePosts(first=first, num=num)
    return jsonify({
        'posts': [post.serialize() for post in posts]
    })
