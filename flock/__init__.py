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
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flock.config import Config

"""
These extensions are not inside create_app()
as they are independent and should be
created outside.

These are then initialized inside create_app()
"""
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()

# Create the app
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flock.users.routes import users
    from flock.posts.routes import posts
    from flock.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app

