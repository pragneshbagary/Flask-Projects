from flask_restful import Resource, fields, marshal_with, reqparse
from database import db, Driver, Log

Driver_fields = {
    'name' : fields.String,
    'license_number' : fields.Integer
}

Log_fields = {
    'start' : fields.Integer,
    'end' : fields.Integer,
    'driver_id': fields.Integer,
    'hours_driven': fields.Integer,
    'voilated' : fields.Boolean
}

Voilations_fields = {
    'name' : fields.String,
    'license_number' : fields.Integer,
    'hours_driven' : fields.Integer,
}


class DriverResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type = str, required = True, help = "name is required")
    parser.add_argument('license_number', type = int, required = True, help = "license number is required")

    @marshal_with(Driver_fields)
    def get(self, driver_id):
        driver = db.session.query(Driver, Log).outerjoin(Driver, Log.driver_id == Driver.id).all()
        result = [
            {
                'driver_name': driver.name if driver else 'Unassigned',
                'start' : log.start,
                'end' : log.end,
            }
            for log, driver in driver
        ]

        return result , 200
    @marshal_with(Driver_fields)
    def post(self):
        data = self.parser.parse_args()
        driver = Driver(name = data['name'], license_number = data['license_number'])
        db.session.add(driver)
        db.session.commit()

        return Driver.query.all()

    
class LogResourece(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('start', type = int, required = True, help = "please enter the start time")
    parser.add_argument('end', type = int, required = True, help = "please enter the end time")
    parser.add_argument('driver_id', type = int, required = True, help = "Please enter driver ID")

    @marshal_with(Log_fields)
    def get(self):
        return Log.query.all()
    
    @marshal_with(Log_fields)
    def post(self):
        data = self.parser.parse_args()
        hours_driven = data['end'] - data['start']
        voilated = True if hours_driven > 11 else False
        log = Log(start = data['start'], end = data['end'], hours_driven = hours_driven, voilated = voilated, driver_id = data['driver_id'])
        db.session.add(log)
        db.session.commit()

        return Log.query.all()
    
class Voilations(Resource):
    @marshal_with(Voilations_fields)
    def get(self):
        violations = db.session.query(Driver, Log).join(Log, Driver.id == Log.driver_id).filter(Log.voilated == True).all()

        for driver, log in violations:
            result =[
                {
                    'name' : driver.name,
                    'license_number' : driver.license_number,
                    'hours_driven' : log.hours_driven
                }
            ]
        return result

    
        
