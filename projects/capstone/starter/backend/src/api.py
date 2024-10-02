import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Employee, Department
from .auth.auth import AuthError, requires_auth
# from auth import AuthError

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
db_drop_and_create_all()

# ROUTES

@app.route("/employees")
@requires_auth('get:employees')
def get_employees():
        employees = Employee.query.all()
        formatted_employees = [emp.short() for emp in employees]
        return jsonify({
            "success": True,
            "employees": formatted_employees
        })

@app.route("/departments")
@requires_auth('get:departments')
def get_departments():
        depts = Department.query.all()
        formatted_departments = [dept.short() for dept in depts]
        return jsonify({
            "success": True,
            "depts": formatted_departments
        })


@app.route('/employee', methods=['POST'])
@requires_auth('post:employee')
def add_employee():
        print('hi')
        data = request.get_json(force=True)
        print(data)
        emp = Employee(
                    name=data.get('name'),
                    location=data.get('location')
                )

        emp = emp.insert()
        return jsonify({
            'success': True
        })

@app.route('/department', methods=['POST'])
@requires_auth('post:department')
def add_employee():
        data = request.get_json(force=True)
        dept = Department(
                    name=data.get('name'),
                    description=data.get('description')
                )

        dept = dept.insert()
        return jsonify({
            'success': True
        })


@app.route('/employees/<id>', methods=['PATCH'])
@requires_auth('patch:employees')
def patch_employee(id):
   data = request.get_json(force=True)
   emp = Employee.query.get_or_404(id)
   emp.location = data.get('location')
   emp.update()
   return jsonify({
            'success': True
        })


@app.route('/employees/<id>', methods=['DELETE'])
@requires_auth('delete:employees')
def delete_employee(id):
   emp = Employee.query.get_or_404(id)
   emp.delete()
   return jsonify({
            'success': True,
            'deleted': id
        })




@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
