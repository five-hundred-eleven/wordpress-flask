from flask import abort, jsonify, request
import json
from pythonwp import app, db, session
from pythonwp.services import user_service
from sqlalchemy.orm import exc as sql_exc


@app.route("/user/login", methods=["POST"])
def login():
    
    user_json = json.loads(request.data).get("user")
    if not user_json:
        abort(1101)

    user_id = user_json.get("user_id")
    user_password = user_json.get("user_password")
    if not user_id and user_password:
        abort(1102)

    try:
        user = user_service.getUser(user_id, user_password)
    except sql_exc.NoResultFound:
        abort(403)

    user_serialized = user.serialize()

    session['user'] = user_serialized
    return jsonify({'user': user_serialized})
