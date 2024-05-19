import json
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)  # Set session lifetime as needed

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Load credentials from config.json
with open('config.json') as config_file:
    config = json.load(config_file)
    app.config['USERNAME'] = config.get("username")
    app.config['PASSWORD'] = config.get("password")

from app import routes, models

with app.app_context():
    db.create_all()