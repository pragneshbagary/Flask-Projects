from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    license_number  = db.Column(db.Integer, nullable = False)
    logs = db.relationship('Log', backref = 'driver', lazy = 'dynamic')

class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable = False)
    start = db.Column(db.Integer, nullable = False)
    end = db.Column(db.Integer, nullable = False)
    hours_driven = db.Column(db.Integer)
    voilated = db.Column(db.Boolean, nullable = True)
    

