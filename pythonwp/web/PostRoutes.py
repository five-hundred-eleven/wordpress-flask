from pythonwp import app
from flask import abort, jsonify, request
from pythonwp.models.Post import Post
from pythonwp.services import post_service

@app.route('/posts', methods=['GET'])
@app.route('/posts/active', methods=['GET'])
def getPosts():

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


@app.route('/posts/all', methods=['GET'])
def getAllPosts():

    first = 0
    if "first" in request.args:
        first = int(request.args.get("first"))
        assert first >= 0

    num = 20
    if "num" in request.args:
        num = int(request.args.get("num"))
        assert first >= 0

    posts = post_service.getBoundedAllPosts(first=first, num=num)
    return jsonify({
        'posts': [post.serializeMinimal() for post in posts]
    })


@app.route('/posts/<int:post_id>', methods=['GET'])
def getPostById(post_id):
    post = post_service.getPostById(post_id)
    return jsonify({
        'post': post.serialize()
    })

@app.route('/posts/<int:post_id>/revisions', methods=['GET'])
def getPostRevisionsById(post_id):
    posts = post_service.getPostRevisionsById(post_id)
    return jsonify({
        'posts': [post.serializeMinimal() for post in posts]
    })
