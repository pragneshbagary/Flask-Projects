from flask import current_app, jsonify
from flask_restful import Resource, marshal_with, fields, reqparse
from models.user import User, db
from werkzeug.security import check_password_hash
import jwt

class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, required = True, help = 'Username required')
    parser.add_argument('password' ,type = str, required = True, help = 'Password required')

    def get(self):
        data = self.parser.parse_args()
        username = data['username']

        user = User.query.filter_by(username=username).first()

        if not user:
            return {'message' : 'No user found'}
        if check_password_hash(user.password,data['password']):
            token = jwt.encode({'id' : user.id}, current_app.config['SECRET_KEY'])
        
            return jsonify({'token': token})
        else: return {'message' : 'incorrect password'}

