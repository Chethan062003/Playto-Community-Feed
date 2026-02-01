# Playto Community Feed

A Reddit-style community feed with threaded comments and a dynamic 24-hour leaderboard.

Built using:

- Django + Django REST Framework
- React (Frontend)
- SQLite Database

---

## 🔧 Backend Setup (Django)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver




Before running the frontend, make sure the Django backend server is running:

cd backend
source venv/bin/activate
python3 manage.py runserver

starting development server at http://127.0.0.1:8000/


http://localhost:8000/admin/

for the admin panel


for the front end in another terminal

cd frontend

npm install

npm start

Local: http://localhost:3000
