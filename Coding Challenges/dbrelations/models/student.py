from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

enrollments = db.Table('enrollments',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    # course = db.relationship('course', backref = 'course', lazy = 'dynamic')
    courses = db.relationship('Course', secondary=enrollments, back_populates='students')


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable = False)
    students = db.relationship('Student', secondary=enrollments, back_populates='courses')


class Teacher(db.Model):
    __tablename__  = 'teacher'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    courses = db.relationship('Course', backref= 'teacher', lazy = 'dynamic')
