from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

# login manager configuration
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config["SECRET_KEY"] = 'c1f105460e4127d0cb0f12a5ab26640a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flaskblog'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
a = app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
b = app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

from flaskblog.routes import routes
