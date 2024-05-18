from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Person

changelog = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/browse')
def browse():
    people = Person.query.all()
    return render_template('browse.html', people=people)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_person = Person(
            full_name=request.form['full_name'],
            nickname=request.form.get('nickname', ''),
            gender=request.form['gender'],
            date_of_birth=request.form.get('date_of_birth', ''),
            place_of_birth=request.form.get('place_of_birth', ''),
            nationality=request.form.get('nationality', ''),
            address=';'.join(request.form.getlist('address')),
            phone_number=request.form.get('phone_number', ''),
            email_address=request.form.get('email_address', ''),
            occupation=request.form.get('occupation', ''),
            company=request.form.get('company', ''),
            job_title=request.form.get('job_title', ''),
            work_address=request.form.get('work_address', ''),
            work_phone_number=request.form.get('work_phone_number', ''),
            work_email_address=request.form.get('work_email_address', ''),
            linkedin_profile=request.form.get('linkedin_profile', ''),
            marital_status=request.form.get('marital_status', ''),
            spouse_name=request.form.get('spouse_name', ''),
            children_names_ages=';'.join(request.form.getlist('children_names_ages')),
            hobbies=request.form.get('hobbies', ''),
            interests=request.form.get('interests', ''),
            favorite_books=';'.join(request.form.getlist('favorite_books')),
            favorite_movies=request.form.get('favorite_movies', ''),
            favorite_music=request.form.get('favorite_music', ''),
            notes=request.form.get('notes', ''),
            social_media_profiles=request.form.get('social_media_profiles', ''),
            date_met=request.form.get('date_met', ''),
            place_met=request.form.get('place_met', ''),
            first_impression=request.form.get('first_impression', ''),
            how_you_met=request.form.get('how_you_met', ''),
            mutual_contacts=';'.join(request.form.getlist('mutual_contacts')),
            last_meeting_date=request.form.get('last_meeting_date', ''),
            next_meeting_date=request.form.get('next_meeting_date', ''),
            image_url=request.form.get('image_url', '')
        )
        db.session.add(new_person)
        db.session.commit()
        changelog.append(f"Added new person: {new_person.full_name}")
        return redirect(url_for('browse'))
    people = Person.query.all()
    return render_template('edit.html', person=None, people=people)

@app.route('/edit/<int:person_id>', methods=['GET', 'POST'])
def edit(person_id):
    person = Person.query.get_or_404(person_id)
    if request.method == 'POST':
        person.full_name = request.form['full_name']
        person.nickname = request.form.get('nickname', '')
        person.gender = request.form['gender']
        person.date_of_birth = request.form.get('date_of_birth', '')
        person.place_of_birth = request.form.get('place_of_birth', '')
        person.nationality = request.form.get('nationality', '')
        person.address = ';'.join(request.form.getlist('address'))
        person.phone_number = request.form.get('phone_number', '')
        person.email_address = request.form.get('email_address', '')
        person.occupation = request.form.get('occupation', '')
        person.company = request.form.get('company', '')
        person.job_title = request.form.get('job_title', '')
        person.work_address = request.form.get('work_address', '')
        person.work_phone_number = request.form.get('work_phone_number', '')
        person.work_email_address = request.form.get('work_email_address', '')
        person.linkedin_profile = request.form.get('linkedin_profile', '')
        person.marital_status = request.form.get('marital_status', '')
        person.spouse_name = request.form.get('spouse_name', '')
        person.children_names_ages = ';'.join(request.form.getlist('children_names_ages'))
        person.hobbies = request.form.get('hobbies', '')
        person.interests = request.form.get('interests', '')
        person.favorite_books = ';'.join(request.form.getlist('favorite_books'))
        person.favorite_movies = request.form.get('favorite_movies', '')
        person.favorite_music = request.form.get('favorite_music', '')
        person.notes = request.form.get('notes', '')
        person.social_media_profiles = request.form.get('social_media_profiles', '')
        person.date_met = request.form.get('date_met', '')
        person.place_met = request.form.get('place_met', '')
        person.first_impression = request.form.get('first_impression', '')
        person.how_you_met = request.form.get('how_you_met', '')
        person.mutual_contacts = ';'.join(request.form.getlist('mutual_contacts'))
        person.last_meeting_date = request.form.get('last_meeting_date', '')
        person.next_meeting_date = request.form.get('next_meeting_date', '')
        person.image_url = request.form.get('image_url', '')
        db.session.commit()
        changelog.append(f"Edited person: {person.full_name}")
        return redirect(url_for('browse'))
    people = Person.query.all()
    return render_template('edit.html', person=person, people=people)

@app.route('/delete/<int:person_id>')
def delete(person_id):
    person = Person.query.get_or_404(person_id)
    changelog.append(f"Deleted person: {person.full_name}")
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('browse'))

@app.route('/changelog')
def changelog_view():
    return render_template('changelog.html', changelog=changelog)