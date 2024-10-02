import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.ext.mutable import Mutable
from sqlalchemy.types import TypeDecorator, TEXT

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    emp = Employee(
        name='John',
        location='UK'
    )
    emp.insert()

    deptt = Department(
        name='IT',
        description='IT description'
    )
    deptt.insert()
# ROUTES

class Employee(db.Model):
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String(80), unique=True)
    location = Column(String(80), unique=True)

    def __init__(self, name, location):
        self.name = name
        self.location = location


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
    
    def short(self):
        return {'id': self.id,'name':self.name,'location': self.location}
    

class Department(db.Model):
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(200), unique=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())    
    
    
    def short(self):
        return {'id': self.id,'name':self.name,'description': self.description}
