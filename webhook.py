from flask import Flask, jsonify, request, make_response
import DataBase as DataBase
import random

'''
Variables
'''
#Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Hail to the Chief we have chosen for the application, \nHail to the Chief! We salute him, one and all."


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)