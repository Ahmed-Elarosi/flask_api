from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


COUNTRIES = {
    "1": {"name": "Austria", "capital": "Vienna"},
    "2": {"name": "Bulgaria", "capital": "Sofia"},
    "3": {"name": "Canada", "capital": "Ottawa"},
    "4": {"name": "Denmark", "capital": "Copenhagen"},
    "5": {"name": "Egypt", "capital": "Cairo"},
    "6": {"name": "Fiji", "capital": "Suva"},
    "7": {"name": "Germany", "capital": "Berlin"},
    "8": {"name": "Haiti", "capital": "Port-au-Prince"},
    "9": {"name": "India", "capital": "New Delhi"},
    "10": {"name": "Japan", "capital": "Tokyo"},
    "11": {"name": "Kenya", "capital": "Nairobi"},
    "12": {"name": "Luxemburg", "capital": "Luxemburg"},
    "13": {"name": "Maldives", "capital": "Male"},
    "14": {"name": "Netherlands", "capital": "Amsterdam"},
    "15": {"name": "Oman", "capital": "Muscat"},
    "16": {"name": "Panama", "capital": "Panama city"},
    "17": {"name": "Qatar", "capital": "Doha"},
    "18": {"name": "Russia", "capital": "Moscow"},
    "19": {"name": "Saint Lucia", "capital": "Castries"},
    "20": {"name": "Turkey", "capital": "Ankara"},
    "21": {"name": "United States", "capital": "Washington D.C"},
    "22": {"name": "Venezuela", "capital": "Caracas"},
    "23": {"name": "Zambia", "capital": "Lusaka"},
    "24": {"name": "United Kingdom", "capital": "London"},
}


class CountriesList(Resource):
    def get(self):
        return COUNTRIES


api.add_resource(CountriesList, "/countries")
