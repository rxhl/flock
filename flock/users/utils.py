import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flock import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)

    # Using _ as placeholder return value as we are not gonna use it anywhere.
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_fn
    )

    # Resize large images
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email],
    )
    msg.body = f"""
        To reset your password, please visit the link below.
        {url_for('users.reset_token', token=token, _external=True)}

        If you did not send this request, please ignore this message and no changes will be made.
    """
    mail.send(msg)
