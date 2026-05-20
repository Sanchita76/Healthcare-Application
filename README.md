# About Project

A complete backend system for a healthcare application using React,  Django, DRF, PostgreSQL, and JWT authentication.

Deployed backend link : https://mediapp-backend-32in.onrender.com/api/auth/register/
---

## Backend Project Architecture
### DFD Level-0 :
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/0c47e0e7-6a35-4711-bc94-92ab344e1ce3" />

### DFD Level-1 :
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/5d05a4a5-91bc-499d-8177-5514305112b0" />

### DFD Level-2 (Auth Service) :
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/44f4e3c9-4cbd-41df-954d-a8dffafe94f2" />
<br> R= Registration , L=Login

### DFD Level-2 (Patient Management):
<img width="510" height="500" alt="image" src="https://github.com/user-attachments/assets/8c76c9ec-671c-4d02-ae74-c2b2419239e1" />

### DFD Level-2 (Doctor Management) :
<img width="532" height="627" alt="image" src="https://github.com/user-attachments/assets/754ee88b-b81d-472c-9200-11d43ad08342" />

### DFD Level-2 (Patient : Doctor Mapping) :
<img width="467" height="630" alt="image" src="https://github.com/user-attachments/assets/dbfc6314-8c9e-4a46-bd3f-acb8c8f4f577" />

                      
## Backend File Architecture Architecture

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

## Testing with Postman 
(Sample API request template given in repository : Healthcare_API.postman_collection.json attached 
=> Open Postman=>Go to Files=>Import the postman collection file and send requests from the collection

### Step 1: Register a User
```
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
    "name": "Mehuli Biswas",
    "email": "mehuli.biswas@gmail.com",
    "password": "-any password-"
}
```
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/a127c273-d8d0-415a-aeec-38c04d3f06f2" />


### Step 2: Login
```
POST http://127.0.0.1:8000/api/auth/login/
Content-Type: application/json

{
    "email": "mehuli.biswas@gmail.com",
    "password": "-any password-"
}
```
Copy the `access` token from the response.
<img width="600" height="505" alt="image" src="https://github.com/user-attachments/assets/3c99d874-fe87-47f6-8542-0260835f9932" />

### Step 3: Use JWT Token
For all authenticated endpoints, add this header:
```
Authorization: Bearer <your_access_token>
```
## Patient Section <br>

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
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/f4546538-8b71-41e3-9458-4ce6de56d600" />

### Step 4: Get All Patients
```
POST http://127.0.0.1:8000/api/patients/
```
<img width="500" height="500" alt="Screenshot 2026-05-19 162109" src="https://github.com/user-attachments/assets/110deb72-2e79-440f-b227-3a06e6a82871" />

### Step 4: Get Patient by ID
```
POST http://127.0.0.1:8000/api/patients/id/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/cd061f78-48cc-4f57-a11b-c74196f779ea" />

### Step 4: Update Patient by ID
```
POST http://127.0.0.1:8000/api/patients/id/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/598b60a4-a504-4861-81ec-b3a1570d54ca" />

### Step 4: Delete Patient by ID
```
POST http://127.0.0.1:8000/api/patients/id/
```
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/d4a7cbe2-4c2f-4c64-8c2d-e26a321ecc54" />

## Doctor Section <br>

### Step 5: Create a Doctor
```
POST http://127.0.0.1:8000/api/doctors/
Authorization: Bearer <token>
Content-Type: application/json
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/d36ca78c-3832-4622-ae03-f773432b61d4" />

### Step 5: Get All Doctors
```
POST http://127.0.0.1:8000/api/doctors/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/506bb874-7b34-4e83-8a95-3600f2c4242c" />

### Step 5: Get Doctor by ID
```
POST http://127.0.0.1:8000/api/doctors/id/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/439a6731-4578-414c-80d6-e5e8af5f951c" />

### Step 5: Update Doctor
```
POST http://127.0.0.1:8000/api/doctors/id/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/ffdb220e-7c4a-4092-adf9-d8dc0d78bdce" />

### Step 5: Update Doctor
```
POST http://127.0.0.1:8000/api/doctors/id/
```
<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/4f15e778-d1ed-4a0e-89ae-89916c3a55c1" />

## Patient Doctor Mappings
### Step 6: Assign Doctor to Patient
```
POST http://127.0.0.1:8000/api/mappings/
Authorization: Bearer <token>
Content-Type: application/json
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7f72dc88-0189-4bce-b727-146eb3494d16" />

### Step 6:Get All Mappings
```
POST http://127.0.0.1:8000/api/mappings/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/c5da9bb4-717c-4b12-86e3-b79815878be4" />

### Step 6: Get Doctor for patient by patient ID
```
POST http://127.0.0.1:8000/api/mappings/patient_id/
```
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/69deed01-708d-48d8-9e14-588c93706e6f" />

### Step 6: Delete Doctor For Patient
```
POST http://127.0.0.1:8000/api/mappings/mapping_id/
```
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/b00e24d6-ffe3-4275-af74-62d3c38f83ad" />
