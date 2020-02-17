# flock

Flock is a twitter clone in flask.

After writing a lot (~20) react/node apps, I thought it would be a good change to write flask. Some of the features of flock includes:

1. Persistent store (sqlite)
2. Session management (Flask-Login)
3. Basic UI using jinja (feels ancient after writing `JSX` for so long)
4. Image upload and editing (Pillow)
5. Pagination support
6. Email and password reset (with JWT)
7. Well defined project structure (venv, packages etc)
8. Hosting (Linode)

## Development

Make sure you have python 3.6 or above.

```
# 1. Clone the project
$ git clone https://github.com/rxhl/flock.git && cd flock

# 2. Create a .env file and fill in the values
$ cp env .env

# 3. Create a virtual environment
$ python3 -m venv venv

# 4. Activate it
$ source ./venv/bin/activate

# 5. Install required packages
$ pip install -r requirements.txt

# 6. Start the flask server
$ python run.py
```

## Email Settings

Flock has an option to let the users reset their passwords. This uses `flask-mail` package which requires a valid email account. We are using Gmail here so after setting the correct values in the `.env` file, make sure to turn on [Less secure app access](https://myaccount.google.com/lesssecureapps) from your Gmail account.

## Courtesy

The amazing Corey Schafer!
