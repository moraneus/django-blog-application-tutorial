# Django Blog Application

This is a simple blog application built with Django. It demonstrates basic CRUD operations (Create, Read, Update, Delete) with Django's models, views, and templates. The application also includes search functionality and utilizes `curl` commands for API testing.
If you want to gets more about this project please visit in my [blog](https://medium.com/@moraneus/introduction-to-python-django-47773b4130e2).

## Project Structure

```plaintext
django-project/
    manage.py
    django-project/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
    blog/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        tests.py
        views.py
        templates/
            blog/
                post_list.html
                post_detail.html
                create_post.html
                update_post.html
        static/
            blog/
                style.css
        urls.py
```

## Setup Instructions
### Prerequisites

* Python 3.x
* Django 3.x or higher


### Installation

1. Clone the repository:
```bash
git clone https://github.com/moraneus/django-blog-application-tutorial.git
cd django-blog-application-tutorial
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash 
pip install django
```

4. Apply migrations:
```bash
python manage.py makemigrations blog
python manage.py migrate 
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver 
```






