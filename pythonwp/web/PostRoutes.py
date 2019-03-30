from pythonwp import app
from flask import abort, jsonify, request
from flask_login import current_user, login_required
import json
from pythonwp.exceptions import AccessDeniedException
from pythonwp.models.Post import Post
from pythonwp.services import post_service
from pythonwp.web import ErrorCodes
from sqlalchemy.orm import exc as sql_exc

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
        'posts': [post.serialize() for post in posts]
    })


@app.route('/posts/<int:post_id>', methods=['GET'])
def getPostById(post_id):

    try:
        post = post_service.getPostById(post_id)
    except sql_exc.NoResultFound:
        abort(ErrorCodes.NOT_FOUND)

    return jsonify({
        'post': post.serialize()
    })

@app.route('/posts/<int:post_id>/revisions', methods=['GET'])
@login_required
def getPostRevisionsById(post_id):
    posts = post_service.getPostRevisionsById(post_id)
    return jsonify({
        'revisions': [post.serialize() for post in posts]
    })

@app.route("/posts/update/<int:post_id>", methods=["POST"])
@login_required
def updatePost(post_id):
    post_json = json.loads(request.data).get("post")
    if not post_json:
        abort(ErrorCodes.BAD_REQUEST)
    try:
        updated_post = post_service.updatePostFromJson(current_user, post_id, post_json)
    except AccessDeniedException:
        abort(ErrorCodes.UNAUTHORIZED)
    except sql_exc.NoResultFound:
        abort(ErrorCodes.NOT_FOUND)

    return jsonify({"post": updated_post.serialize()})

@app.route("/posts/new", methods=["POST"])
@login_required
def newPost():
    post_json = json.loads(request.data).get("post")
    if not post_json:
        abort(ErrorCodes.BAD_REQUEST)
    try:
        new_post = post_service.newPostFromJson(current_user, post_json)
    except AccessDeniedException:
        abort(ErrorCodes.UNAUTHORIZED)
    except sql_exc.NoResultFound:
        abort(ErrorCodes.NOT_FOUND)

    return jsonify({"post": new_post.serialize()})
