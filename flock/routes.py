from flask import render_template, url_for, flash, redirect
from flock import app
from flock.forms import RegistrationForm, LoginForm
from flock.models import User, Post

posts = [
    {
        "author": "James Madison",
        "title": "Blog Post 1",
        "content": "lorem ipsum",
        "date_posted": "Feb 9, 2020",
    },
    {
        "author": "Max Lowe",
        "title": "Blog Post 2",
        "content": "lorem ipsum",
        "date_posted": "Feb 9, 2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "a@a.com" and form.password.data == "admin":
            flash(f"Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Login failed!", "danger")
    return render_template("login.html", title="Login", form=form)
