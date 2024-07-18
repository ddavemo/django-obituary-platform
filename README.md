# Obituary Platform

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Setup](#setup)
5. [Development Process](#development-process)
6. [Usage](#usage)
7. [Database Management](#database-management)
8. [Customization](#customization)
9. [Troubleshooting](#troubleshooting)

## Introduction

The Obituary Platform is a web application built with Django and PostgreSQL, designed for submitting, managing, and displaying obituaries. In this case I used GNU/Linux to develop the application

## Features

- User-friendly interface for submitting and viewing obituaries
- Responsive design with light and dark themes
- PostgreSQL database for robust data storage
- Pagination for efficient browsing of obituaries
- SEO-friendly structure
- Admin interface for easy management

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)
- virtualenv (recommended but is optional)

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/ddavemo/obituary-platform.git
    cd obituary-platform
    ```

2. Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # Linux
    ```

    On Windows, use:

    ```
    venv\Scripts\activate
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:

    ```
    sudo -u postgres psql
    CREATE DATABASE obituary_platform;
    CREATE USER david WITH PASSWORD 'momanyi';
    ALTER ROLE david SET client_encoding TO 'utf8';
    ALTER ROLE david SET default_transaction_isolation TO 'read committed';
    ALTER ROLE david SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE obituary_platform TO david;
    \q  # to quit
    ```

5. Update the database configuration in `obituary_project/settings.py`:

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'obituary_platform',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

6. Run migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Create a superuser:

    ```
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```
    python manage.py runserver
    ```

## Development Process

- Set up the Django project and app structure
- Design and implement the database model for obituaries
- Create views for submitting and viewing obituaries
- Develop templates for the user interface
- Implement pagination for efficient browsing
- Add theme switching functionality (light/dark mode)
- Optimize for SEO
- Implement responsive design for various screen sizes

## Usage

- Access the admin panel at `http://localhost:8000/admin/` to manage obituaries
- Visit `http://localhost:8000/` to view obituaries
- Go to `http://localhost:8000/submit/` to submit a new obituary

## Database Management

To view or modify the database directly:

Connect to PostgreSQL:

```
sudo -u postgres psql obituary_platform
```
*You may be required to input a password*

View all obituaries:

```
SELECT * FROM obituaries_obituary;
```

Delete an obituary:

```
DELETE FROM obituaries_obituary WHERE id = <obituary_id>;
```

## Customization

- Modify the CSS in `obituaries/static/css/styles.css` to change the appearance
- Update templates in `obituaries/templates/` to alter the HTML structure
- Adjust the model in `obituaries/models.py` for different obituary fields

## Troubleshooting

- If you encounter database permission issues, ensure your PostgreSQL user has the correct privileges
- For static file issues, run `python manage.py collectstatic`
- Clear your browser cache if you don't see CSS changes

