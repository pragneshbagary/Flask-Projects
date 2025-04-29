from flask_restful import Resource, reqparse, fields, marshal_with
from database import db, Vehicle, Driver


Vehicle_fields = {
    'vin' : fields.Integer,
    'driver_id': fields.Integer
}

Driver_fields = {
    'name' : fields.String
}

class VehicleResourse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('vin', type = int, required=True, help='VIN is required')
    parser.add_argument('driver_id' , type = int, required = False)

    @marshal_with(Vehicle_fields)
    def get(self):
        return Vehicle.query.all()
    
    # @marshal_with
    # def get(self, vehicle_id):
    #     return Vehicle.query.filter_by(vehicle_id=vehicle_id).first()
    
    @marshal_with(Vehicle_fields)
    def post(self):
        data = self.parser.parse_args()
        print(data)
        if Vehicle.query.filter_by(vin=data['vin']).first():
            return {'error': 'VIN already exists'}, 400
        if data['driver_id'] and not Driver.query.get(data['driver_id']):
            return {'error': 'Driver not found'}, 404
        vehicle = Vehicle(vin = data['vin'], driver_id = data['driver_id'])
        db.session.add(vehicle)
        db.session.commit()
        print("vehicle added")

        return Vehicle.query.all()
    
class DriverResourse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type = str, required = True, help = "There is no name")

    @marshal_with(Driver_fields)
    def get(self):
        return Driver.query.all()
    
    # @marshal_with
    # def get(self, driver_id):
    #     driver = Driver.query.get(driver_id)
    #     if driver:
    #         return {'id': driver.id, 'name': driver.name, 'license_number': driver.license_number}, 200
    #     return {'error': 'Driver not found'}, 404
    
    @marshal_with(Driver_fields)
    def post(self):
        data = self.parser.parse_args()
        driver = Driver(name = data['name'])
        db.session.add(driver)
        db.session.commit()

        return Driver.query.all()

class VehicleDriverList(Resource):
    @marshal_with(Vehicle_fields)
    def get(self, driver_id):
        vehicles = db.session.query(Vehicle, Driver).outerjoin(Driver, Vehicle.driver_id == Driver.id).all()
        result = [
            {
                'vehicle_id': vehicle.id,
                'vin': vehicle.vin,
                'driver_name': driver.name if driver else 'Unassigned',
            }
            for vehicle, driver in vehicles
        ]
        return result, 200

