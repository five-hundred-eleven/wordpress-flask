from pythonwp import app
from flask import abort, jsonify, request
from pythonwp.models.Post import Post
from pythonwp.services import page_service
from sqlalchemy.orm import exc as sql_exc

@app.route('/pages', methods=['GET'])
def getPages():

    if "name" in request.args:

        try:
            page = page_service.getPageByName(request.args["name"])
        except sql_exc.NoResultFound:
            abort(404)

        return jsonify({
            'page': page.serialize()
        })

    else:
        pages = page_service.getActivePages()
        return jsonify({
            'pages': [page.serialize() for page in pages]
        })

@app.route('/pages/<int:page_id>', methods=['GET'])
def getPageById(post_id):

    try:
        page = page_service.getPageById(page_id)
    except sql_exc.NoResultFound:
        abort(404)

    return jsonify({
        'page': page.serialize()
    })
