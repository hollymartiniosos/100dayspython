#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


def main():

    #1. Ściągnij wszystkie dane z sheety z klasy
    sheety_data_manager = DataManager()
    sheety_data = sheety_data_manager.get_sheety_data()
    flight_search_manager = FlightSearch()
    flight_data_manager = FlightData()
    twilio_manager = NotificationManager()

    #2. Dla każdego rzędu w danych: 
    for row in sheety_data:
    #a. czy ma iata code
        if row["iataCode"] == '':
    #b. jeśli nie znajdź code 
            code = flight_search_manager.get_IATA_code(row['city'])
    #c. wstaw code do sheety
            row["iataCode"] = code 
            sheety_data_manager.set_IATA_code(row["id"], code)
    print(sheety_data)

    for row in sheety_data:
        flights = flight_data_manager.search_flights(row["iataCode"], row["lowestPrice"])
        print(f'{len(flights)} under {row["lowestPrice"]} to {row["city"]} found.')
        if len(flights) > 0:
            best_flight = flights[0]
            print(best_flight)
            flight_info = {
                "price": best_flight["price"] ,
                "departure_city_name":best_flight["cityFrom"] ,
                "departure_airport_iata_code":best_flight["cityCodeFrom"] ,
                "arrival_city_name":best_flight["cityTo"] ,
                "arrival_airport_iata_code":best_flight["cityCodeTo"] ,
                "outbound_date":str(best_flight["route"][0]["local_departure"]).split("T")[0] ,
                "inbound_date":str(best_flight["route"][-1]["local_departure"]).split("T")[0] ,
            }
            print(flight_info)
            twilio_manager.send_SMS(flight_info=flight_info)
if __name__=="__main__":
    main()
