# Business CRM System

A simple console-based Customer Relationship Management (CRM) system built with Python and MySQL.

## Features

- User registration and login
- Password hashing with bcrypt
- Add, view, update, delete, and search customers
- Add and view leads
- Update lead status
- MySQL database integration
- Environment variables for database credentials

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- bcrypt
- python-dotenv
- Git & GitHub

## Project Structure

```text
crm_system/
│
├── app.py
├── auth.py
├── customers.py
├── database.py
├── followups.py
├── leads.py
├── requirements.txt
├── .gitignore
└── .env

.env is not included in the GitHub repository because it contains sensitive database credentials.

How to Run
Clone the repository.
Create a Python virtual environment.
Install the required packages:
pip install -r requirements.txt
Create a .env file in the project root:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=business_crm
Make sure the MySQL database business_crm exists.
Run:
python app.py
Purpose

This project was built as a beginner-friendly Python project to practice:

Python functions and modules
CRUD operations
MySQL database interaction
Authentication
Password hashing
Environment variables
Git and GitHub