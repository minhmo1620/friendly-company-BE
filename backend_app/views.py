from flask_restful import Resource

dummy_data = ["Hello", "World", "Hi"]

class get_data(Resource):
    def get(self):
        return {'data':dummy_data}, 200