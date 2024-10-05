# Backend - capstone API

## Setting up the Backend

### Install Dependencies

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `api.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With sqllite running, create a `capstone` database:

```bash
createdb capstone
```

Populate the database using the `setup.db` file provided. From the `backend` folder in terminal run:


### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_app.py`

## Usage

## endpoints
GET http://127.0.0.1:5000/employees

RESPONSE

{
    "success": True,
    "employees": []
}

GET http://127.0.0.1:5000/departments

RESPONSE

{
    "success": True,
    "departments": []
}

DELETE http://127.0.0.1:5000/employees/1

RESPONSE

{
    "deleted": 1,
    "success": True
}

POST http://127.0.0.1:5000/employee

Request

        {
            name='q1',
            location='a1'
        }

Response

        {
          "success": True
        }

POST http://127.0.0.1:5000/department

Request

        {
            name='q1',
            description='a1'
        }

Response

        {
          "success": True
        }       

POST http://127.0.0.1:5000/employees/1

Request

        {
            name='q2',
            location='a2'
        }

Response

        {
          "success": True
        }

## App has been deployed to Heroku -
https://capstone-app-diid-c72c9116ab15.herokuapp.com/