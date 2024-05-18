from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Person

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/browse')
def browse():
    people = Person.query.all()
    return render_template('browse.html', people=people)

@app.route('/add', methods=['GET', 'POST'])
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def add_or_edit(id=None):
    person = Person.query.get(id) if id else None
    if request.method == 'POST':
        if person:
            # Update existing person
            person.full_name = request.form['full_name']
            person.nickname = request.form['nickname']
            person.gender = request.form['gender']
            person.date_of_birth = request.form['date_of_birth']
            person.place_of_birth = request.form['place_of_birth']
            person.nationality = request.form['nationality']
            person.address = request.form['address']
            person.phone_number = request.form['phone_number']
            person.email_address = request.form['email_address']
            person.image_url = request.form['image_url']
            person.occupation = request.form['occupation']
            person.company = request.form['company']
            person.job_title = request.form['job_title']
            person.work_address = request.form['work_address']
            person.work_phone_number = request.form['work_phone_number']
            person.work_email_address = request.form['work_email_address']
            person.linkedin_profile = request.form['linkedin_profile']
            person.marital_status = request.form['marital_status']
            person.spouse_name = request.form['spouse_name']
            person.children_names_ages = request.form['children_names_ages']
            person.hobbies = request.form['hobbies']
            person.interests = request.form['interests']
            person.favorite_books = request.form['favorite_books']
            person.favorite_movies = request.form['favorite_movies']
            person.favorite_music = request.form['favorite_music']
            person.notes = request.form['notes']
            person.social_media_profiles = request.form['social_media_profiles']
            person.date_met = request.form['date_met']
            person.place_met = request.form['place_met']
            person.first_impression = request.form['first_impression']
            person.how_you_met = request.form['how_you_met']
            person.mutual_contacts = request.form['mutual_contacts']
            person.last_meeting_date = request.form['last_meeting_date']
            person.next_meeting_date = request.form['next_meeting_date']
        else:
            # Add new person
            new_person = Person(
                full_name=request.form['full_name'],
                nickname=request.form['nickname'],
                gender=request.form['gender'],
                date_of_birth=request.form['date_of_birth'],
                place_of_birth=request.form['place_of_birth'],
                nationality=request.form['nationality'],
                address=request.form['address'],
                phone_number=request.form['phone_number'],
                email_address=request.form['email_address'],
                image_url=request.form['image_url'],
                occupation=request.form['occupation'],
                company=request.form['company'],
                job_title=request.form['job_title'],
                work_address=request.form['work_address'],
                work_phone_number=request.form['work_phone_number'],
                work_email_address=request.form['work_email_address'],
                linkedin_profile=request.form['linkedin_profile'],
                marital_status=request.form['marital_status'],
                spouse_name=request.form['spouse_name'],
                children_names_ages=request.form['children_names_ages'],
                hobbies=request.form['hobbies'],
                interests=request.form['interests'],
                favorite_books=request.form['favorite_books'],
                favorite_movies=request.form['favorite_movies'],
                favorite_music=request.form['favorite_music'],
                notes=request.form['notes'],
                social_media_profiles=request.form['social_media_profiles'],
                date_met=request.form['date_met'],
                place_met=request.form['place_met'],
                first_impression=request.form['first_impression'],
                how_you_met=request.form['how_you_met'],
                mutual_contacts=request.form['mutual_contacts'],
                last_meeting_date=request.form['last_meeting_date'],
                next_meeting_date=request.form['next_meeting_date']
            )
            db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('browse'))
    return render_template('edit.html', person=person)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('browse'))