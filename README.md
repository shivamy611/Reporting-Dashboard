# Reporting Dashboard Backend

Django (models, migrations, admin) + FastAPI (REST API) on MySQL. Both share the same Django ORM models.

## Setup (after installing MySQL)
1. `pip install -r requirements.txt`
2. Create the database: `CREATE DATABASE reporting_dashboard CHARACTER SET utf8mb4;`
3. Edit `.env` (DB_USER / DB_PASSWORD etc.)
4. `python manage.py migrate`
5. `python manage.py createsuperuser`

## Run
- FastAPI: `uvicorn api.main:app --reload --port 8000` -> docs at http://localhost:8000/docs
- Django admin: `python manage.py runserver 8001` -> http://localhost:8001/admin
