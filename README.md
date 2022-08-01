# Bloggers Social Network

The project allows you to view and publish author's articles with an image, by category.

There is registration and authorization of users. Redefined standard forms for registration and authorization.

An authorized user can leave reviews on articles and comments on reviews, subscribe to authors and manage their subscriptions.

Redefined standard server error pages, performed optimization and caching.


This is the final version of the project.

API for the social network of authors is made in a separate repository https://github.com/web2cap/api_yamdb/


Сloned from: https://github.com/web2cap/hw04_tests

### Includes applications

 - posts: articles by authors and categories of articles, reviews and comments
 - about: static pages
 - core: context processors 
 - users: reimplemented authorization and registration forms, user subscriptions

## Technology:

Python and Django
Bootstrap
Pytest

## Installation
Clone the repository and change into it on the command line:
```
git clone https://github.com/web2cap/hw02_community.git
```

```
cd hw02_community
```

Create and activate virtual environment:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Install dependencies from requirements.txt file:

```
pip install -r requirements.txt
```

Run migrations:

```
python3 manage.py migrate
```

You can create a super user:

```
python3 manage.py createsuperuser
```

Run project:

```
python3 manage.py runserver
```

## Author

Pavel Koshelev