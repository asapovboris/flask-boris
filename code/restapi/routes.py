from flask import request
from . import app, connection
from .models import get_user, update_user

user_id = 1

@app.route("/api/v1/hello", methods=["GET", "POST", "PUT"])
def Hello():
    username = get_user(connection, user_id)

    if request.method == 'POST':
        if not 'Username' in request.json:
            return "no Username specified in json format"
        else:
            return "hello " + request.json['Username']
    elif request.method == 'PUT':
        if not 'Username' in request.json:
            return "no Username specified in json format"
        else:
            username = request.json['Username']
            update_user(connection, user_id, request.json['Username'])
            return "username updated to " + username
    else:
        return "hello " + username


