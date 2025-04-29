from flask_restful import Resource, marshal_with, fields, reqparse
from models.student import Course as c, db

course_fields = {
    'name' : fields.String,
    'teacher_id' : fields.String,
    'teacher' : fields.String

}

class Courses(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required = True, help = 'Name is required')
    parser.add_argument('teacher_id', type=int, required = True, help = 'Teacher id is required')

    @marshal_with(course_fields)
    def get(self):
        return c.query.all()
    
    @marshal_with(course_fields)
    def post(self):
        data = self.parser.parse_args()
        tourse = c(name = data['name'], teacher_id = data['teacher_id'])
        db.session.add(tourse)
        db.session.commit()

        return c.query.all()
    