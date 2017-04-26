#~ version one of the mailMorth api which would hold all the functionalities of our version one
#(@: Name): "mailMorth"

#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence Protective Rights please edit and use it with all the care you can give

#import blueprint class


from flask import Blueprint
from flask_restplus import Resource, Api, reqparse
#end all import
api_v1 = Blueprint('api_v1', __name__)#create a blueprint structure of the flask class
mailApi=Api(api_v1)#initialize the api class by passing the flask object to it
#start routin pages here

@mailApi.route("/")
class main(Resource):
	"""docstring for main"Resource"""
	def get(self):
		# return {"request":"success"}
		return {"client":{"version":1.0,"response":200}}