# Employee App

A simple Django application for demonstrating a basic employee API project.

## Overview
This project contains a Django application with an employee-related endpoint and a clean project structure for further development.

## Features
- Django project setup
- Basic employee list endpoint
- Easy to extend with models, views, and templates

## Tech Stack
- Python
- Django
- PostgreSQL support via psycopg2-binary

## Setup
1. Create and activate a virtual environment:
   - `python -m venv env`
   - `env\Scripts\activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply database migrations:
   - `python manage.py migrate`
4. Start the development server:
   - `python manage.py runserver`

## Usage
Open your browser and visit:
- `http://127.0.0.1:8000/`

This route currently returns a simple response for the employee list endpoint.

## Project Structure
- `employee_api/` - main app containing views, URLs, and future models
- `employee_app/` - Django project settings and configuration
- `manage.py` - command-line utility for Django
