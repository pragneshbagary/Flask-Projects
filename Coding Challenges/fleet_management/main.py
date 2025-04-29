from flask import Flask
from flask_restful import Api
from database import db
from resources import VehicleResourse,  DriverResourse, VehicleDriverList


app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fleet.db'

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(VehicleResourse, '/vehicles')
api.add_resource(DriverResourse, '/drivers')
api.add_resource(VehicleDriverList, '/list')


if __name__ == '__main__':
    app.run(debug=True)


