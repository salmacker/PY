import os
from dotenv import find_dotenv, load_dotenv
from amadeus import Client, ResponseError, Location

class FlightData:
    
    # [to modify] def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = 0
        self.IATA_dep = departure
        # Load environement variables
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]

    def find_cheapest_flight(data):
        # to add

        # return cheapest_flight (FlightData class)

    