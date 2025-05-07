from flask_restful import Resource
from flask import jsonify
from app.decorators.authentication import token_required

class ProtectedResource(Resource):
    @token_required
    def get(current_user, self):  # Note: current_user comes from the decorator
        return jsonify({
            'message': f'Hello, {current_user.username}!',
            'id': current_user.id
        })
