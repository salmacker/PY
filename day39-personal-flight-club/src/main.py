#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from data_manager import DataManager
from flight_search import FlightSearch
import pandas as pd

data_manager = DataManager()
destinations = data_manager.read_IATA()
flight_search = FlightSearch()

# Iterate over the 'Name' column
for index, row in destinations.iterrows():
    if pd.isna(row['iataCode']):
        city = row['City']
        IATA = flight_search.getIata(city)
        destinations.at[index, 'iataCode'] = IATA

data_manager.write_IATA(destinations)
