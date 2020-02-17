"""
Here we are converting flock from a module (flock.py) to a package (flock/__init__.py)

A Python module is simply a Python source file, which can expose classes, functions and global variables. 
When imported from another Python source file, the file name is treated as a namespace.
A Python package is simply a directory of Python module(s).

And so we can use: 
from flock.X import A, B, C

More generally:
from mypackage.mymodule import myclass
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = os.getenv("EMAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("EMAIL_PORT")
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASS")
mail = Mail(app)

"""
Avoid flask circular imports
"""
from flock import routes
