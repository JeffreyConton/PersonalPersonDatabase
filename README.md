# Personal Person Database

This project is a web-based personal person database application that allows you to store, browse, and manage information about people you have met. The application is built using Flask, SQLAlchemy, and Flask-Login.

## Features

- User authentication with login and logout functionality.
- Add, edit, and delete person records.
- Store comprehensive information about each person, including basic info, contact details, professional details, and personal interests.
- Pagination support for browsing people.
- Login required to access any part of the application.

## Installation

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/personal-person-database.git
    cd personal-person-database
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `config.json` file in the root directory with the following content:**

    ```json
    {
        "username": "admin",
        "password": "password"
    }
    ```

5. **Initialize the database:**

    ```sh
    python init_db.py
    ```

6. **Run the application:**

    ```sh
    python run.py
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000/login`.

## Usage

### Login

1. Navigate to the login page (`http://127.0.0.1:5000/login`).
2. Enter the username and password specified in the `config.json` file.
3. Click "Login" to access the application.

### Add a Person

1. Click on the "Add Person" link in the navigation menu.
2. Fill out the form with the person's details.
3. Click "Save" to add the person to the database.

### Browse People

1. Click on the "Browse" link in the navigation menu.
2. View the list of people in the database. Use the pagination controls to navigate through the pages.

### Edit a Person

1. In the browse view, click the "Edit" button next to the person you want to edit.
2. Update the person's details in the form.
3. Click "Save" to apply the changes.

### Delete a Person

1. In the browse view, click the "Delete" button next to the person you want to delete.
2. Confirm the deletion to remove the person from the database.

## Project Structure

