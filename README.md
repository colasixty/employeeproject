Install python

Install Django

Install postgresql

Install Postman

Install dependencies like: djangorestframework, faker, psycopg_binary

Create database mydb with psql or pgadmin

CREATE DATABASE mydb;
CREATE USER myuser WITH PASSWORD '12345678';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser; 

GRANT USAGE ON SCHEMA public TO myuser;
GRANT CREATE ON SCHEMA public TO myuser;

Run the following commands

python manage.py makemigrations
python manage.py migrate
python manage.py generate_employees
python manage.py runserver

Running Postman, check the following enpoints:

http://127.0.0.1:8000/api/average-salary/

Response:

{
    "average_salary": 86896.83
}

http://127.0.0.1:8000/api/department-summary/

Response:

[
    {
        "department": "SALES",
        "count": 10
    },
    {
        "department": "HR",
        "count": 13
    },
    {
        "department": "ENG",
        "count": 14
    },
    {
        "department": "FIN",
        "count": 7
    },
    {
        "department": "MKT",
        "count": 6
    }
]

http://127.0.0.1:8000/api/attendance/

Response:

[
    {
        "id": 1,
        "date": "2025-07-08",
        "check_in": "10:54:46",
        "check_out": "18:54:46",
        "employee": 1001
    },
    ...
]

http://127.0.0.1:8000/api/leaves/

Response:

[
    {
        "id": 1,
        "start_date": "2025-05-29",
        "end_date": "2025-05-31",
        "leave_type": "VACATION",
        "reason": "Enter sea upon song ability help raise research.",
        "employee": 1001
    },
    ...
]