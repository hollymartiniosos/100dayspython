import os
import requests
from datetime import datetime as dt
from datetime import timedelta as td 



KIWI_ID = os.environ["KIWI_ID"]
KIWI_KEY = os.environ["KIWI_API_KEY"]
KIWI_API = "https://api.tequila.kiwi.com/"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, 
                 origin_airport_code: str = "BNE",
                 trip_duration: tuple[int,int] = (7,28), 
                 currency: str = "AUD") -> None:
        
        self.headers = {
            "apikey": KIWI_KEY 
            }
        self.origin_airport_code= origin_airport_code
        self.trip_duration = trip_duration
        self.currency=currency
          

    def search_flights(self, destination_code: str, price: int, max_stopovers: int = 2, via_city: str = "") -> list:
        #Znajdź loty dla destynacji z sheety
        params = {
            "fly_from": self.origin_airport_code,
            "fly_to": destination_code,
            "date_from": (dt.now()+td(days=1)).strftime("%d/%m/%Y"),
            "date_to": (dt.now()+td(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": self.trip_duration[0],
            "nights_in_dst_to": self.trip_duration[1],
            "flight_type": "round",
            "curr": self.currency, 
            "price_to": price,
            "max_stopovers": max_stopovers,
            "via_city": via_city



        }
        response = requests.get(f'{KIWI_API}v2/search', params=params, headers=self.headers)
        if response.status_code == 200:
            print("Successfully fetched the data")
            flights = response.json()['data']
            
            return flights
        else:
            print(f'Failed {response.status_code}')
            return []
   
        
if __name__ == "__main__":
    cos3 = FlightData()
    print(cos3.search_flights("WAW", 1000))

        