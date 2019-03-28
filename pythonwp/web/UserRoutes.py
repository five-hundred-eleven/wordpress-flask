from flask import abort, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
import json
from pythonwp import app, db, login, session
from pythonwp.web import ErrorCodes
from pythonwp.exceptions import InvalidPasswordException
from pythonwp.services import user_service
from sqlalchemy.orm import exc as sql_exc


@app.route("/user/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
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
    login_user(user, remember=user_serialized)

    return jsonify({'user': user_serialized})

@app.route("/user/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"user": None})

@app.route("/user/session", methods=["GET"])
@login_required
def getUserSession():
    return jsonify({"user": current_user.serialize()})

@app.route("/user/password", methods=["POST"])
@login_required
def updatePassword():
    user_json = json.loads(request.data).get("user")
    if not user_json:
        abort(ErrorCodes.BAD_REQUEST)

    username = user_json.get("username")
    if username != current_user.user_nicename:
        abort(ErrorCodes.UNAUTHORIZED)

    old_password = user_json.get("old_password")
    new_password = user_json.get("new_password")
    if not old_password or not new_password:
        abort(ErrorCodes.BAD_REQUEST)

    try:
        user_service.updatePassword(current_user.user_id, old_password, new_password)
    except InvalidPasswordException:
        abort(ErrorCodes.UNAUTHORIZED)

    return jsonify({'user': current_user.serialize()})
