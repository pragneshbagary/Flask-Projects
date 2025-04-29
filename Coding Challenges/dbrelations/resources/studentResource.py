from flask_restful import Resource, fields, marshal_with, reqparse
from models.student import Student as st, db, Course as c, enrollments as e
from flask import request

student_fields = {
    'name' : fields.String
}

enroll_fields = {
    'name' : fields.Integer,
    'course': fields.Integer
}

class Students(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required = True, help = 'Name is required')
    
    @marshal_with(student_fields)
    def get(self):
        return st.query.all()
    
    @marshal_with(student_fields)
    def post(self):
        data = self.parser.parse_args()
        student = st(name = data['name'])
        db.session.add(student)
        db.session.commit()
        
        return st.query.all()
    
class Student(Resource):
    @marshal_with(student_fields)
    def get(self, id):
        return st.query.filter_by(id = id).first()
    

    

        
    
    
        


