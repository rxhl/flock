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

app = Flask(__name__)
app.config["SECRET_KEY"] = "892627b4f69774cf4859685cdea0e6b5"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

"""
Avoid flask circular imports
"""
from flock import routes
