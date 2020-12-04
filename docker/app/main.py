# -*- coding: utf-8 -*-
import json
import datetime
import requests
from flask import Flask
from flask import Response
from flask import request
from flask import jsonify, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Sample(Resource):
    def get(self):
        return make_response("OK", 200)

if __name__ == "__main__":
    api.add_resource(Sample, '/')
    app.run(host='0.0.0.0',port=80, debug=True)
