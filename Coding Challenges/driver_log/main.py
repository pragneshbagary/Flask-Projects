from flask import Flask
from flask_restful import Api
from database import db
from resources import DriverResource, LogResourece, Voilations

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///driverlog.db'

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()
    
api.add_resource(DriverResource, '/drivers/')
api.add_resource(LogResourece, '/logs')
api.add_resource(Voilations, '/voilations')

if __name__ == '__main__':
    app.run(debug=True)