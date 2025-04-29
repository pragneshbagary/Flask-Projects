from flask import Flask
from models.student import db
from flask_restful import Api
from resources.studentResource import Students
from resources.enrollmentResource import EnrollStudent, CourseList, StudentList
from resources.teacherResource import Teachers, GetCourses
from resources.courseResource import Courses

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()


api.add_resource(Students, '/students')
api.add_resource(Teachers, '/teachers')
api.add_resource(Courses, '/courses')
api.add_resource(GetCourses, '/teachers/<int:id>')
api.add_resource(EnrollStudent, '/students/enroll')
api.add_resource(CourseList, '/courselist/<int:id>')
api.add_resource(StudentList, '/studentlist/<int:id>')


if __name__ == '__main__':
 app.run(debug=True)