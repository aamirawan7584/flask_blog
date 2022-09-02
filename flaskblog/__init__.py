from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "167dfcb89982be0cb2bf3d9ac4c2cb03"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# DONT EVER INCLUDE SENSITIVE INFORMATION IN CODE AND USE IT FROM SYSTEM VARIABLE.
app.config['MAIL_USERNAME']=os.environ.get('FLASK_EMAIL')
app.config['MAIL_PASSWORD']= os.environ.get('FLASK_EMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



mail = Mail(app)

from flaskblog import routes
