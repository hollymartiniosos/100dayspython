import os
import requests
import json
from twilio.rest import Client
KIWI_ID = os.environ["KIWI_ID"]
KIWI_KEY = os.environ["KIWI_API_KEY"]
KIWI_API = "api.tequila.kiwi.com/v2/search"
SHEETY_API = os.environ["SHEETY_PRICES_API"]
SHEETY_TOKEN = os.environ["SHEETY_PRICES_TOKEN"]

print(KIWI_ID, KIWI_KEY, SHEETY_API, SHEETY_TOKEN)

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def get_sheety_data(self) -> list:
        bearer_headers = {
            "Authorization": f'Bearer {SHEETY_TOKEN}' 
        }

        response = requests.get(SHEETY_API, headers=bearer_headers)
        if response.status_code == 200:
            print("Successfully fetched the data")
            sheety_prices = response.json()
            sheet_data = sheety_prices["prices"]
            return sheet_data
        else:
            print(f'Failed {response.status_code}') 
            return []
        

    def set_IATA_code(self, row_id: int, IATA_code: str): 
        bearer_headers = {
            "Authorization": f'Bearer {SHEETY_TOKEN}' 
        }
        params= { 
            "price":{
                'iataCode': IATA_code
            }
        }
        response = requests.put(f'{SHEETY_API}/{row_id}', headers=bearer_headers, json=params)
        if response.status_code == 200:
            print("Successfully changed the data")
            
        else:
            print(f'Failed {response.json()}') 


if __name__ == "__main__":
    cos2 = DataManager()
    print(cos2.get_sheety_data())
    print(cos2.set_IATA_code(5, "LMA"))

    