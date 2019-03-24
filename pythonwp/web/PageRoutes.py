from pythonwp import app
from flask import abort, jsonify, request
from pythonwp.models.Post import Post
from pythonwp.services import page_service

@app.route('/pages', methods=['GET'])
def getPages():

    if "name" in request.args:
        page = page_service.getPageByName(request.args["name"])
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
    page = page_service.getPageById(page_id)
    return jsonify({
        'page': page.serialize()
    })
