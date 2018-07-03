import re
class Validator():
    def __init__(self, obj , actity):
        self.ride_ofer_props = ["name","From","To","car_model","cost","seats_available", "time", ]
        self.ride_request_props = ["name", "From", "To", "seats_needed", "time"]
        self.register_props = ["name","username","email", "password"]
        self.has_numbers = re.compile('[0-9]')
        self.has_special = re.compile('[^\w\s]')
        self.activity=actity
        self.obj = obj

    def validate(self):
        if self.activity == 'create_ride':
            for prop in self.ride_ofer_props:
                if prop not in self.obj:
                    return {"message": f"please provide {prop}"}

                if self.obj[prop].strip() == "":
                    return {'message': f"empty{prop} not allowed"}

                if len(str(self.obj['name'])) > 100:
                    return {'message': "name should not be more than 100 characters"}

                if self.has_numbers.search(self.obj['name']) or self.has_special.search(self.obj['name']):
                    return {'message': 'name should not contain numbers or special character'}

        if self.activity == 'request_ride':
            for prop in self.ride_request_props:
                if prop not in self.obj:
                    return {"message": f"please provide {prop}"}

                if self.obj[prop].strip() == "":
                    return {'message': f"empty{prop} not allowed"}

                if len(str(self.obj['name'])) > 100:
                    return {'message': "name should not be more than 100 characters"}

                if self.has_numbers.search(self.obj['name']) or self.has_special.search(self.obj['name']):
                    return {'message': 'name should not contain numbers or special character'}

        if self.activity  == 'reg':
            for prop in self.register_props:
                if prop not in self.obj:
                    return {"message": f"please provide {prop}"}
            for prop in self.register_props:
                if self.obj[prop].strip()=="":
                    return {'message': f"empty{prop} not allowed"}

                if len(str(self.obj['name'])) > 100:
                    return {'message': "name should not be more than 100 characters"}
                
                if '@' not in str(self.obj['email']):
                    return {"message":"Email is invalid"}

                if '.' not in str(self.obj['email']):
                    return {"message":"Email is invalid"}

                if len(str(self.obj['password'])) < 8:
                    return {"message":"password cannot be less than 8 characters"}
                if not self.has_numbers.search(self.obj['password']):
                    return {"message":"password must have atlist one number"}
                if len(str(self.obj['password'])) > 150:
                    return  {'message': "password should not be more than 150 characters"}

                if len(str(self.obj['username'])) > 10:
                    return {'message': "username should not be greater than 10 characters"}

                if self.has_numbers.search(self.obj['name']):
                    return {'message': "name should not contain numbers"}
                
                if self.has_special.search(self.obj['name']):
                    return {'message': "name should not contain special chars"}
