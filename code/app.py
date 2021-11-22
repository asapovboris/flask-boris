from flask import Flask
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blahblahblah'

username = ""

if __name__ == '__main__':
    @app.route("/api/v1/hello", methods=["GET", "POST", "PUT"])
    def Hello():
        global username
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
                return "username updated to " + username
        else:
            return "hello " + username


    app.run(debug=True)
    # app.run(host='0.0.0.0')
