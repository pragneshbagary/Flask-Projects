from flask_restful import Resource, marshal_with, fields, reqparse
from app.models import *
from app.extensions import db
from werkzeug.security import generate_password_hash

userFields = {
    'id' :  fields.Integer,
    'username' : fields.String,
    'password' :  fields.String,
}

class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, required = True, help = 'Username required')
    parser.add_argument('password', type = str, required = True, help = 'Password required')
    
    # @marshal_with(userFields)
    def post(self):
        data = self.parser.parse_args()
        username = data.get('username')
        if User.query.filter_by(username = username).first():
            return {'message' : 'username taken, please try with new username'}, 400
        hashed_password = generate_password_hash(data['password'], method = 'pbkdf2:sha256')
        newuser = User(username = data['username'], password = hashed_password)

        db.session.add(newuser)
        db.session.commit()
        return {'message' : 'user created sucessfully'}, 201
    
    @marshal_with(userFields)
    def get(self):
        return User.query.all()


        
