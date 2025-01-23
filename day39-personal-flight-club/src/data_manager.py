import pandas as pd

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        pass

    def read_IATA(self):
        df = pd.read_csv('../data/flight_destination.csv')
        df['iataCode'] = df['iataCode'].astype('object')
        return df

    def write_IATA(self, df):
        df.to_csv('../data/flight_destination.csv', index=False)

    
