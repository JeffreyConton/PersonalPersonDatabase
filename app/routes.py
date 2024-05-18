from flask import Flask, render_template, request, redirect, url_for
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
    if id:
        person = Person.query.get_or_404(id)
    else:
        person = None

    if request.method == 'POST':
        if not person:
            person = Person()

        person.full_name = request.form['full_name']
        person.nickname = request.form['nickname']
        person.gender = request.form['gender']
        person.date_of_birth = request.form['date_of_birth']
        person.place_of_birth = request.form['place_of_birth']
        person.nationality = request.form['nationality']
        person.address = ';'.join(request.form.getlist('address'))
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
        person.children_names_ages = ';'.join(request.form.getlist('children_names_ages'))
        person.hobbies = request.form['hobbies']
        person.interests = request.form['interests']
        person.favorite_books = ';'.join(request.form.getlist('favorite_books'))
        person.favorite_movies = request.form['favorite_movies']
        person.favorite_music = request.form['favorite_music']
        person.notes = request.form['notes']
        person.social_media_profiles = request.form['social_media_profiles']
        person.date_met = request.form['date_met']
        person.place_met = request.form['place_met']
        person.first_impression = request.form['first_impression']
        person.how_you_met = request.form['how_you_met']
        person.mutual_contacts = ';'.join(request.form.getlist('mutual_contacts'))
        person.last_meeting_date = request.form['last_meeting_date']
        person.next_meeting_date = request.form['next_meeting_date']

        db.session.add(person)
        db.session.commit()

        return redirect(url_for('browse'))

    return render_template('edit.html', person=person, people=Person.query.all())

@app.route('/delete/<int:id>')
def delete(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('browse'))