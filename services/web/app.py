from flask import Flask, render_template, request, redirect, url_for, json
from flask_sqlalchemy import SQLAlchemy
import geocoder
import os


app = Flask(__name__)
app.debug = False


# placeholder for index page
@app.route('/')
def index():

    return 'Welcome to Geolocator App'


# returns json version of .shp file converted to postgresql database
@app.route('/geodata')
def geodata():
    root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(root, "", "state_geodata.json")
    data = json.load(open(json_url))
    return json.jsonify(data) 


# user inputs address and gets geodata returned in JSON format
@app.route('/<address>', methods=['GET'])
def geolocator(address):
    g = geocoder.mapquest(address, key=MAPQUEST_KEY).json

    addy = g['address']
    zip = g['postal']
    lat = g['lat']
    long = g['lng']
    city = g['city']
    state = g['state']

    geo_dict = {
        'address': addy,
        'zip': zip,
        'lat': lat,
        'long': long,
        'city': city,
        'state': state
        }

    return geo_dict


if __name__ == "__main__":
    app.run()