from app.extensions import db

class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key = True)
    todo = db.Column(db.String(500), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    