from flask import Flask
import pymysql.cursors

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PnjDc7vmaNHmuxMi6Tw2m1g6FBhiTdWNxR8jOleZFxk'

sql_username = 'sqluser'
sql_password = 'A123456A'
sql_host = 'localhost'
sql_port = '3306'
sql_database = 'restapi'

# Connect to the database
connection = pymysql.connect(host=sql_host,
                             user=sql_username,
                             password=sql_password,
                             database=sql_database,
                             cursorclass=pymysql.cursors.DictCursor)

from . import routes