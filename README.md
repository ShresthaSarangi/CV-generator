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

## 📸 Screenshots

### Home Page

<img width="1912" height="939" alt="front_page png" src="https://github.com/user-attachments/assets/a32264af-d797-4d5f-a446-c7e8194f3f3f" />


### Generated CV

<img width="1895" height="947" alt="CV png" src="https://github.com/user-attachments/assets/b209d1ca-9b14-47dd-81d2-5568d7b42e1e" />
<img width="1898" height="943" alt="CV1 png" src="https://github.com/user-attachments/assets/27e51735-3e67-4511-a482-55e41882d862" />


### Create CV Page
<img width="1919" height="942" alt="create png" src="https://github.com/user-attachments/assets/7fff4b60-0aa0-4240-aaaf-0632262e753a" />



## Author

**Shrestha Sarangi**

GitHub: https://github.com/ShresthaSarangi
