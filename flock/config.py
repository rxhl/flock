import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = os.getenv("EMAIL_SERVER")
    MAIL_PORT = os.getenv("EMAIL_PORT")
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASS")
