from flask import Flask
from flask_mysqldb import MySQL

from settings import MYSQL_CURSORCLASS, MYSQL_DB, MYSQL_PASSWORD, MYSQL_USER, MYSQL_UNIX_SOCKET, MYSQL_HOST 

app = Flask(__name__)

app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_UNIX_SOCKET'] = MYSQL_UNIX_SOCKET
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = MYSQL_CURSORCLASS

db = MySQL(app)

from authentication import authentication
from places import places
from detection import detection

#TEST
@app.route('/')
def hello():
    return 'Welcome to GuideMe Private EndPoint'

app.register_blueprint(authentication, url_prefix="/api/auth")

app.register_blueprint(places, url_prefix="/api/get")

app.register_blueprint(detection, url_prefix="/api/detection")

