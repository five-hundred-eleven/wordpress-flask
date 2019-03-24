from flask import abort, jsonify, request
import json
from pythonwp import app, db, session
from pythonwp.web import ErrorCodes
from pythonwp.exceptions import InvalidPasswordException
from pythonwp.services import user_service
from sqlalchemy.orm import exc as sql_exc


@app.route("/user/login", methods=["POST"])
def login():

    if session.get("user"):
        abort(ErrorCodes.FORBIDDEN)

    user_json = json.loads(request.data).get("user")
    if not user_json:
        abort(ErrorCodes.BAD_REQUEST)

    user_id = user_json.get("user_id")
    user_password = user_json.get("user_password")
    if not user_id and user_password:
        abort(ErrorCodes.BAD_REQUEST)

    try:
        user = user_service.getUser(user_id, user_password)
    except sql_exc.NoResultFound:
        abort(ErrorCodes.NOT_FOUND)
    except InvalidPasswordException:
        abort(ErrorCodes.UNAUTHORIZED)

    user_serialized = user.serialize()

    session['user'] = user_serialized
    return jsonify({'user': user_serialized})

@app.route("/user/getsession", methods=["GET"])
def getUserSession():
    return jsonify({'user': session.get('user')})
