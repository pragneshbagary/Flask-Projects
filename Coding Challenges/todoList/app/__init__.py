from flask import Flask
from app.extensions import db
from flask_restful import Api
from app.resources import *

def create_app():
    app =Flask('__name__')
    app.config['SECRET_KEY'] = 'mynameispragnesh'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    # db = SQLAlchemy(app)
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return "This is the Home Page!!!"

    api.add_resource(Login, '/login')
    api.add_resource(Register, '/register')
    api.add_resource(ProtectedResource, '/homepage')
    api.add_resource(TodoResource, '/user/todo')

    return app 