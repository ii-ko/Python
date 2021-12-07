from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import secrets


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flaskblog'

from flaskblog.routes import routes

