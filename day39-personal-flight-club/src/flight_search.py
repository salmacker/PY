import os
from dotenv import find_dotenv, load_dotenv
from amadeus import Client, ResponseError, Location

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # Load environement variables
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]

    def findIata(self, city):
        # Initiate the client
        amadeus = Client(client_id=self._api_key, client_secret=self._api_secret)
        try:
            response = amadeus.reference_data.locations.get(keyword=city, subType=Location.ANY)
            return(response.data[0]["iataCode"])

        except ResponseError as error:
            print(error)
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        # to add

    