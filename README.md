# CV Generator

A Django-based web application that allows users to create, edit, manage, and download their CVs easily. Users can fill in their details, generate a professional CV, make changes whenever required, and download it as a PDF file. Created using pre-defined templates.

## Features

* Create a new CV
* Edit existing CV details
* Delete CV
* Generate CV dynamically
* Download CV as PDF
* Manage personal, educational, and professional details

## Tech Used

* Python
* Django
* HTML
* Tailwind CSS
* SQLite

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/ShresthaSarangi/cv-generator.git
```

2. Go to the project directory

```bash
cd cv-generator
```

3. Create a virtual environment

```bash
python -m venv env
```

Activate it:

**Windows**

```bash
env\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Apply migrations

```bash
python manage.py migrate
```

6. Run the development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## Project Structure

```
cv-generator/
│
├── manage.py
├── db.sqlite3
├── users/
├── cv/
├── templates/
└── mysite/
```

## Author

**Shrestha Sarangi**

GitHub: https://github.com/ShresthaSarangi
