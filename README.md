# Healthcare Backend

A complete backend system for a healthcare application using Django, DRF, PostgreSQL, and JWT authentication.

---

## Project Architecture

```
healthcare_backend/
├── healthcare_backend/          # project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── authentication/          # User registration & login
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── patients/                # Patient management
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── doctors/                 # Doctor management
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── mappings/                # Patient-Doctor mappings
│       ├── __init__.py
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── .env                         # Environment variables
├── requirements.txt
└── manage.py
```

---

## Prerequisites

- Python 3.9+
- PostgreSQL 13+
- pip

---

## Step-by-Step Setup

### 1. Install PostgreSQL (if not installed)

**Windows:** Download installer from https://www.postgresql.org/download/windows/

---

### 2. Create PostgreSQL Database and User

```bash

# Run these SQL commands:
CREATE DATABASE healthcare_db;
CREATE USER healthcare_user WITH PASSWORD 'your_secure_password';
ALTER ROLE healthcare_user SET client_encoding TO 'utf8';
ALTER ROLE healthcare_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE healthcare_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;
\q
```

---

### 3. Clone / Create Project Directory

```bash
mkdir healthcare_backend
cd healthcare_backend
```

---

### 4. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate - Windows
venv\Scripts\activate
```

---

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Configure Environment Variables

Edit `.env`:
```
SECRET_KEY=your-very-long-random-secret-key-here
DEBUG=True
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

**Generate a secure SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### 7. Run Migrations

```bash
python manage.py makemigrations authentication
python manage.py makemigrations patients
python manage.py makemigrations doctors
python manage.py makemigrations mappings
python manage.py migrate
```

---

### 8. Create Superuser (Proper Management of Database)

---

### 9. Run the Development Server

```bash
python manage.py runserver
```
available at: `http://127.0.0.1:8000/`

---

## API Endpoints Reference

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Login & get JWT token | No |

### Patients

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/patients/` | Create a patient | Yes |
| GET | `/api/patients/` | List all patients (own) | Yes |
| GET | `/api/patients/<id>/` | Get patient details | Yes |
| PUT | `/api/patients/<id>/` | Update patient | Yes |
| DELETE | `/api/patients/<id>/` | Delete patient | Yes |

### Doctors

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/doctors/` | Create a doctor | Yes |
| GET | `/api/doctors/` | List all doctors | Yes |
| GET | `/api/doctors/<id>/` | Get doctor details | Yes |
| PUT | `/api/doctors/<id>/` | Update doctor | Yes |
| DELETE | `/api/doctors/<id>/` | Delete doctor | Yes |

### Patient-Doctor Mappings

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/mappings/` | Assign doctor to patient | Yes |
| GET | `/api/mappings/` | Get all mappings | Yes |
| GET | `/api/mappings/<patient_id>/` | Get doctors for patient | Yes |
| DELETE | `/api/mappings/<id>/` | Remove mapping | Yes |

---

## Testing with Postman (Sample API requests : Healthcare_API.postman_collection/json attached)

### Step 1: Register a User
```
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "SecurePass123"
}
```

### Step 2: Login
```
POST http://127.0.0.1:8000/api/auth/login/
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "SecurePass123"
}
```
Copy the `access` token from the response.

### Step 3: Use JWT Token
For all authenticated endpoints, add this header:
```
Authorization: Bearer <your_access_token>
```

### Step 4: Create a Patient
```
POST http://127.0.0.1:8000/api/patients/
Authorization: Bearer <token>
Content-Type: application/json

{
    "name": "Alice Smith",
    "age": 30,
    "gender": "Female",
    "address": "123 Main St",
    "phone": "9876543210",
    "medical_history": "Diabetes"
}
```

### Step 5: Create a Doctor
```
POST http://127.0.0.1:8000/api/doctors/
Authorization: Bearer <token>
Content-Type: application/json

{
    "name": "Dr. Bob Jones",
    "specialization": "Endocrinology",
    "phone": "9123456789",
    "email": "drjones@hospital.com",
    "experience_years": 10
}
```

### Step 6: Assign Doctor to Patient
```
POST http://127.0.0.1:8000/api/mappings/
Authorization: Bearer <token>
Content-Type: application/json

{
    "patient": 1,
    "doctor": 1
}
```