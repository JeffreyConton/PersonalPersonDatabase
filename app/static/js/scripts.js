<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% if person %}Edit Person{% else %}Add Person{% endif %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <div class="container">
        <div class="navigation">
            <h2>Navigation</h2>
            <ul>
                <li><a href="{{ url_for('browse') }}">Back</a></li>
            </ul>
        </div>
        <div class="content">
            <div class="form-container">
                <h2>{% if person %}Edit{% else %}Add{% endif %} Person</h2>
                <form method="post">
                    <div class="dropdown-section">
                        <div class="dropdown-header" onclick="toggleDropdown(this)">
                            <h3>Basic Information</h3>
                            <span class="toggle-icon">+</span>
                        </div>
                        <div class="dropdown-content">
                            <div class="form-group">
                                <label for="full_name">Full Name:</label>
                                <input type="text" id="full_name" name="full_name" value="{{ person.full_name if person else '' }}" required>
                            </div>
                            <div class="form-group">
                                <label for="nickname">Nickname:</label>
                                <input type="text" id="nickname" name="nickname" value="{{ person.nickname if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="gender">Gender:</label>
                                <select id="gender" name="gender">
                                    <option value="Male" {% if person and person.gender == "Male" %}selected{% endif %}>Male</option>
                                    <option value="Female" {% if person and person.gender == "Female" %}selected{% endif %}>Female</option>
                                    <option value="Other" {% if person and person.gender == "Other" %}selected{% endif %}>Other</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="date_of_birth">Date of Birth:</label>
                                <input type="date" id="date_of_birth" name="date_of_birth" value="{{ person.date_of_birth if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="place_of_birth">Place of Birth:</label>
                                <input type="text" id="place_of_birth" name="place_of_birth" value="{{ person.place_of_birth if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="nationality">Nationality:</label>
                                <input type="text" id="nationality" name="nationality" value="{{ person.nationality if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="address">Address:</label>
                                <div id="address-container">
                                    {% if person and person.address %}
                                        {% for address in person.address.split(';') %}
                                            <input type="text" name="address" value="{{ address }}">
                                        {% endfor %}
                                    {% else %}
                                        <input type="text" name="address" value="">
                                    {% endif %}
                                </div>
                                <button type="button" class="add-btn" onclick="addField('address-container', 'address')">Add Address</button>
                            </div>
                            <div class="form-group">
                                <label for="phone_number">Phone Number:</label>
                                <input type="text" id="phone_number" name="phone_number" value="{{ person.phone_number if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="email_address">Email Address:</label>
                                <input type="email" id="email_address" name="email_address" value="{{ person.email_address if person else '' }}">
                            </div>
                        </div>
                    </div>

                    <div class="dropdown-section">
                        <div class="dropdown-header" onclick="toggleDropdown(this)">
                            <h3>Professional Information</h3>
                            <span class="toggle-icon">+</span>
                        </div>
                        <div class="dropdown-content">
                            <div class="form-group">
                                <label for="occupation">Occupation:</label>
                                <input type="text" id="occupation" name="occupation" value="{{ person.occupation if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="company">Company:</label>
                                <input type="text" id="company" name="company" value="{{ person.company if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="job_title">Job Title:</label>
                                <input type="text" id="job_title" name="job_title" value="{{ person.job_title if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="work_address">Work Address:</label>
                                <input type="text" id="work_address" name="work_address" value="{{ person.work_address if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="work_phone_number">Work Phone Number:</label>
                                <input type="text" id="work_phone_number" name="work_phone_number" value="{{ person.work_phone_number if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="work_email_address">Work Email Address:</label>
                                <input type="email" id="work_email_address" name="work_email_address" value="{{ person.work_email_address if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="linkedin_profile">LinkedIn Profile:</label>
                                <input type="text" id="linkedin_profile" name="linkedin_profile" value="{{ person.linkedin_profile if person else '' }}">
                            </div>
                        </div>
                    </div>

                    <div class="dropdown-section">
                        <div class="dropdown-header" onclick="toggleDropdown(this)">
                            <h3>Personal Information</h3>
                            <span class="toggle-icon">+</span>
                        </div>
                        <div class="dropdown-content">
                            <div class="form-group">
                                <label for="marital_status">Marital Status:</label>
                                <select id="marital_status" name="marital_status">
                                    <option value="Single" {% if person and person.marital_status == "Single" %}selected{% endif %}>Single</option>
                                    <option value="Married" {% if person and person.marital_status == "Married" %}selected{% endif %}>Married</option>
                                    <option value="Divorced" {% if person and person.marital_status == "Divorced" %}selected{% endif %}>Divorced</option>
                                    <option value="Widowed" {% if person and person.marital_status == "Widowed" %}selected{% endif %}>Widowed</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="spouse_name">Spouse's Name:</label>
                                <input type="text" id="spouse_name" name="spouse_name" value="{{ person.spouse_name if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="children_names_ages">Children's Names and Ages:</label>
                                <textarea id="children_names_ages" name="children_names_ages">{{ person.children_names_ages if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="hobbies">Hobbies:</label>
                                <textarea id="hobbies" name="hobbies">{{ person.hobbies if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="interests">Interests:</label>
                                <textarea id="interests" name="interests">{{ person.interests if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="favorite_books">Favorite Books:</label>
                                <div id="favorite-books-container">
                                    {% if person and person.favorite_books %}
                                        {% for book in person.favorite_books.split(';') %}
                                            <input type="text" name="favorite_books" value="{{ book }}">
                                        {% endfor %}
                                    {% else %}
                                        <input type="text" name="favorite_books" value="">
                                    {% endif %}
                                </div>
                                <button type="button" class="add-btn" onclick="addField('favorite-books-container', 'favorite_books')">Add Book</button>
                            </div>
                            <div class="form-group">
                                <label for="favorite_movies">Favorite Movies:</label>
                                <textarea id="favorite_movies" name="favorite_movies">{{ person.favorite_movies if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="favorite_music">Favorite Music:</label>
                                <textarea id="favorite_music" name="favorite_music">{{ person.favorite_music if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="notes">Notes:</label>
                                <textarea id="notes" name="notes">{{ person.notes if person else '' }}"></textarea>
                            </div>
                        </div>
                    </div>

                    <div class="dropdown-section">
                        <div class="dropdown-header" onclick="toggleDropdown(this)">
                            <h3>Meeting Information</h3>
                            <span class="toggle-icon">+</span>
                        </div>
                        <div class="dropdown-content">
                            <div class="form-group">
                                <label for="date_met">Date Met:</label>
                                <input type="date" id="date_met" name="date_met" value="{{ person.date_met if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="place_met">Place Met:</label>
                                <input type="text" id="place_met" name="place_met" value="{{ person.place_met if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="first_impression">First Impression:</label>
                                <textarea id="first_impression" name="first_impression">{{ person.first_impression if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="how_you_met">How You Met:</label>
                                <textarea id="how_you_met" name="how_you_met">{{ person.how_you_met if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="mutual_contacts">Mutual Contacts:</label>
                                <textarea id="mutual_contacts" name="mutual_contacts">{{ person.mutual_contacts if person else '' }}"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="last_meeting_date">Last Meeting Date:</label>
                                <input type="date" id="last_meeting_date" name="last_meeting_date" value="{{ person.last_meeting_date if person else '' }}">
                            </div>
                            <div class="form-group">
                                <label for="next_meeting_date">Next Meeting Date:</label>
                                <input type="date" id="next_meeting_date" name="next_meeting_date" value="{{ person.next_meeting_date if person else '' }}">
                            </div>
                        </div>
                    </div>

                    <button type="submit">{% if person %}Update{% else %}Add{% endif %}</button>
                </form>
            </div>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
    <script>
        function toggleDropdown(header) {
            const content = header.nextElementSibling;
            const icon = header.querySelector('.toggle-icon');
            if (content.classList.contains('show')) {
                content.classList.remove('show');
                icon.textContent = '+';
            } else {
                content.classList.add('show');
                icon.textContent = '-';
            }
        }

        function addField(containerId, fieldName) {
            const container = document.getElementById(containerId);
            const input = document.createElement('input');
            input.type = 'text';
            input.name = fieldName;
            container.appendChild(input);
        }
    </script>
</body>
</html>