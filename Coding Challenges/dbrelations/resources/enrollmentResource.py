from flask_restful import Resource, fields, marshal_with, reqparse
from models.student import Student as st, db, Course as c, enrollments as e
from flask import request

course_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

student_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

class EnrollStudent(Resource):       
    def post(self):
        data = request.get_json()
        student_id = data['student_id']
        course_id = data['course_id']

        student = st.query.get(student_id)
        course = c.query.get(course_id)

        if not student or not course:
            return {"message": "Student or Course not found"}, 404

        student.courses.append(course)
        db.session.commit()

        return {"message": f"Student {student.name} enrolled in {course.name}"}, 200
    
class CourseList(Resource):
    @marshal_with(course_fields)
    def get(self, id):
        student = st.query.filter_by(id = id).first()

        return student.courses, 200
    
class StudentList(Resource):
    @marshal_with(student_fields)
    def get(self, id):
        course = c.query.filter_by(id = id).first()

        return course.students , 200