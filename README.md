# Flask Rest API
This program shows how to set up a flaskrestapi with postgres_db, blueprint, sqlalchemy, marshmallow, wsgi, unittests

# Install guide

### Clone the repo

```$ git clone https://github.com/bisratyalew/flask-rest-api.git```
```$ cd flask-rest-api```

### Create the virtualenv

```$ mkvirtualenv flask-rest-api```

### Install dependencies

```$ pip install -r requirements.txt```

### Running on development machine
```
python manage.py runserver
```

### Features

* Rest Api Flask App
* Serialize object into response
* Integration with Flask-IO to parse parameters from request
* Configuration per environment
* Integration with SQL Alchemy
* Uses Postgres DB
* Unit tests per module