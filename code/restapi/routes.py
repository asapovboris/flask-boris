from flask import request
from . import app, connection
from .models import get_user, update_user, add_user
from .tools import check_id_valid, id_generator, check_input
import simplejson as json

user_id = 1

@app.route("/")
def index():
    return "Simple Rest API server by Boris Asapov"

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

@app.route("/api/v1/add-user", methods=["POST"])
def AddUser():
    if request.method == 'POST':
        if not 'Username' in request.json:
            return "no Username specified in json format"
        else:
            add = add_user(connection, request.json['Username'])
            return add

@app.route("/api/v1/check-id", methods=["POST"])
def CheckID():
    if request.method == 'POST':
        if not 'ID' in request.json or not request.json['ID']:
            return "no ID variable specified"
        else:
            check = check_id_valid(request.json['ID'])
            if check:
                return str(request.json['ID']) + " is a valid ID"
            else:
                return str(request.json['ID']) + " is not a valid ID"

@app.route("/api/v1/id-generator", methods=["POST"])
def IDGenerator():
    if request.method == 'POST':
        if not 'ID' in request.json or not request.json['ID']:
            return "no ID variable specified"
        check = check_input(request.json['ID'])
        if check:
            return check
        else:
            gen = id_generator(int(request.json['ID']))
            # return ' '.join(gen)
            list1 = json.dumps((i for i in list(gen)), iterable_as_array=True)
            return list1
