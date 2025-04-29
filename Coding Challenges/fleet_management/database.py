from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    vin = db.Column(db.Integer, nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=True)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    vehicles = db.relationship('Vehicle', backref = 'driver', lazy = True)



