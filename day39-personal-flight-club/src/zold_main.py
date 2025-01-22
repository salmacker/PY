#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from dotenv import find_dotenv, load_dotenv

import requests
from amadeus import Client, ResponseError

# find .env automatically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")

amadeus = Client(
    client_id=AMADEUS_API_KEY,
    client_secret=AMADEUS_API_SECRET
)

try:
    flights = amadeus.shopping.flight_offers_search.get(
        originLocationCode='WAW',
        destinationLocationCode='NYC',
        departureDate='2025-04-01',
        adults=1).data
    response_one_flight = amadeus.shopping.flight_offers.pricing.post(
        flights[0])
    print(response_one_flight.data)

except ResponseError as error:
    print(error)



# url = "https://api.sheety.co/69cf9c6d8fb772f1596f52f492476bbb/flightDeals/prices"
# response = requests.get(url)


# if response.status_code == 200:
#    data = response.json()
#    # Do something with the data
#    print(data)
# else:
#    print(f"Failed to fetch data: {response.status_code}")

