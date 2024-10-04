import os
import unittest
import json
from flask.app import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from database.models import db_drop_and_create_all, setup_db, Employee, Department
from auth.auth import AuthError, requires_auth
# from auth import AuthError

app = Flask(__name__)
setup_db(app)
CORS(app)


db_drop_and_create_all()


class APITestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        setup_db(app)
        CORS(app)
        db_drop_and_create_all()
        self.app = app
        self.client = self.app.test_client
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_employees(self):
        res = self.client().get('/employees')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['employees'])
        self.assertTrue(len(data['employees']))

    def test_404_get_employees(self):
        res = self.client().get('/employeess')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')  

        def test_get_departments(self):
            res = self.client().get('/departments')
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['departments'])
            self.assertTrue(len(data['departments']))

    def test_404_get_departments(self):
        res = self.client().get('/departmentss')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found') 
   

    def test_delete_employee(self):
        res = self.client().delete('/employees/1')
        print(res.status_code)
        if(res.status_code == 200):
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
        else:
            self.assertEqual(res.status_code, 500)
        

    def test_404_delete_employee(self):
        res = self.client().get('/employee/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')     

    def test_successful_employee_creation(self):
        # Given
        payload = json.dumps({
            "name": "name1",
            "location": "L1"
        })

        # When
        response = self.client().post('/employee', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(True, response.json['success'])
        self.assertEqual(200, response.status_code)     

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()