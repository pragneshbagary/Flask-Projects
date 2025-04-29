from flask_restful import Resource, marshal_with, fields, reqparse
from models.student import Teacher as t, db, Course as c

teacher_fields = {
    'name' : fields.String
}

course_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class Teachers(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required = True, help = 'Name is required')

    @marshal_with(teacher_fields)
    def get(self):
        return t.query.all()
    
    @marshal_with(teacher_fields)
    def post(self):
        data = self.parser.parse_args()
        teacher = t(name = data['name'])
        db.session.add(teacher)
        db.session.commit()

        return t.query.all()

class GetCourses(Resource):
    @marshal_with(course_fields)
    def get(seld, id):
       return c.query.filter_by(teacher_id = id).all()
        
        
    