from flask import Flask
from models.user import db
from flask_restful import Api
from resources.login import Login
from resources.register import Register


app =Flask('__name__')
app.config['SECRET_KEY'] = 'mynameispragnesh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "This is the Home Page!!!"

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
# api.add_resource(Register, '/register/<int:id>')

if __name__ == '__main__':
    app.run(debug = True)