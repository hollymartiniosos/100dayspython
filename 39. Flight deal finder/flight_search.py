import os
import requests


KIWI_ID = os.environ["KIWI_ID"]
KIWI_KEY = os.environ["KIWI_API_KEY"]
KIWI_API = "https://api.tequila.kiwi.com/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_IATA_code(self, city_name: str) -> str:
        headers = {
        "apikey": KIWI_KEY 
        }
        params = {
            "term": city_name,
            "location_types": "city"

        }
        response = requests.get(KIWI_API+"locations/query", params=params, headers=headers)
        if response.status_code == 200:
            print("Successfully fetched the data")
            city_info = response.json()
            city_code = city_info["locations"][0]["code"]
            print(city_code)
            return city_code
            
        else:
            print(f'Failed {response.status_code}')
            return "UNKNOWN"  

if __name__ == "__main__":
    cos = FlightSearch()
    cos.get_IATA_code("BRISBANE")    

    