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

@app.route("/user/password", methods=["POST"])
def updatePassword():
    user_json = json.loads(request.data).get("user")
    if not user_json:
        abort(ErrorCodes.BAD_REQUEST)

    username = user_json.get("username")
    if username != session['user']['user_nicename']:
        abort(ErrorCodes.UNAUTHORIZED)

    old_password = user_json.get("old_password")
    new_password = user_json.get("new_password")
    if not old_password or not new_password:
        abort(ErrorCodes.BAD_REQUEST)

    try:
        user_service.updatePassword(session['user']['user_id'], old_password, new_password)
    except InvalidPasswordException:
        abort(ErrorCodes.UNAUTHORIZED)

    return jsonify({'user': session['user']})


@app.route("/user/session", methods=["GET"])
def getUserSession():
    return jsonify({'user': session.get('user')})

@app.route("/user/logout", methods=["POST"])
def logout():
    session["user"] = None;
    return jsonify({"user": None})
