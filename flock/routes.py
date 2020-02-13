from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

# Direct import from __init__.py file
from flock import app, db, bcrypt

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
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(
            f"Account created for {form.username.data}! Please log in now.", "success"
        )
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        # Session management
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")

            # Ternary op
            return redirect(next_page) if next_page else redirect(url_for("home"))
        flash(f"Login failed!", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")
