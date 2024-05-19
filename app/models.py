from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    gender = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    place_of_birth = db.Column(db.String(100))
    nationality = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(50))
    email_address = db.Column(db.String(100))
    image_url = db.Column(db.String(200))
    occupation = db.Column(db.String(100))
    company = db.Column(db.String(100))
    job_title = db.Column(db.String(100))
    work_address = db.Column(db.String(200))
    work_phone_number = db.Column(db.String(50))
    work_email_address = db.Column(db.String(100))
    linkedin_profile = db.Column(db.String(200))
    marital_status = db.Column(db.String(50))
    spouse_name = db.Column(db.String(100))
    children_names_ages = db.Column(db.String(200))
    hobbies = db.Column(db.String(200))
    interests = db.Column(db.String(200))
    favorite_books = db.Column(db.String(200))
    favorite_movies = db.Column(db.String(200))
    favorite_music = db.Column(db.String(200))
    notes = db.Column(db.String(200))
    social_media_profiles = db.Column(db.String(200))
    date_met = db.Column(db.Date)
    place_met = db.Column(db.String(100))
    first_impression = db.Column(db.String(200))
    how_you_met = db.Column(db.String(200))
    mutual_contacts = db.Column(db.String(200))
    last_meeting_date = db.Column(db.Date)
    next_meeting_date = db.Column(db.Date)