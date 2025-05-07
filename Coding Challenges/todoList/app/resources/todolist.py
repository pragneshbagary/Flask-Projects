from flask_restful import Resource, reqparse, marshal_with, fields
from app.decorators.authentication import token_required
from app.models import *
from app.extensions import db

todo_fields = {
    'id' : fields.Integer,
    'todo' : fields.String,
    'user_id' : fields.Integer
}

class TodoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('todo', type = str, required = True, help = 'Enter the task')

    @token_required
    @marshal_with(todo_fields)
    def get(current_user, self):
        if not current_user: return {"message" : "user not recognized"}, 403
        user_id = current_user.id
        return Todo.query.filter_by(user_id = user_id).all()
    
    @token_required
    @marshal_with(todo_fields)
    def post(current_user, self):
        if not current_user: return {"message" : "user not recognized"}, 403
        data = self.parser.parse_args()
        user_id = current_user.id
        new_todo = Todo(todo = data['todo'], user_id = user_id)
        db.session.add(new_todo)
        db.session.commit()

        return Todo.query.filter_by(user_id = user_id).all()
        

