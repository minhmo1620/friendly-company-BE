from flask import Flask
from .views import get_data
from flask_restful import Api


app = Flask(__name__)
api = Api(app) 

api.add_resource(get_data, '/getdata')
app.run(debug=True, port=5000)