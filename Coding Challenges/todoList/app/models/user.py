from  app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String, nullable = False)
    token = db.Column(db.String, nullable = True)
    todo = db.relationship('Todo', backref = 'user', lazy = True)