from flask import Flask
import os

app = Flask(__name__, static_folder='../build', static_url_path='/')
config = dict(os.environ)
app.secret_key = config['SECRET_KEY']

from app import routes