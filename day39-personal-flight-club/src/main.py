#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests

url = "https://api.sheety.co/69cf9c6d8fb772f1596f52f492476bbb/flightDeals/prices"
response = requests.get(url)


if response.status_code == 200:
   data = response.json()
   # Do something with the data
   pprint(data)
else:
   pprint(f"Failed to fetch data: {response.status_code}")