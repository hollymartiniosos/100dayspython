#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from users import User

def extract_stopovers(flight_dict):
    return_flag_list =  [flight["return"] for flight in flight_dict["route"]]
    num_stopovers = (return_flag_list.count(0) -1 , return_flag_list.count(1) -1)
    flights_out = [flight for flight in flight_dict["route"] if flight["return"] == 0]
    so_out = [flight["flyTo"] for flight in flights_out[:-1]]
    flights_in = [flight for flight in flight_dict["route"] if flight["return"] == 1]
    so_in = [flight["flyTo"] for flight in flights_in[:-1]]

    return num_stopovers, so_out, so_in

def main():

    #1. Ściągnij wszystkie dane z sheety z klasy
    sheety_data_manager = DataManager()
    sheety_data = sheety_data_manager.get_sheety_data()
    flight_search_manager = FlightSearch()
    flight_data_manager = FlightData()
    twilio_manager = NotificationManager()
    user_manager = User()
    user_info = user_manager.users_info()


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
        current_stopovers = 0
        flights = []
        while current_stopovers<= 2 and len(flights) < 1: 
            flights = flight_data_manager.search_flights(row["iataCode"], row["lowestPrice"], max_stopovers=current_stopovers*2) 
            print(f'{len(flights)} under {row["lowestPrice"]} to {row["city"]} found with {current_stopovers} stopovers.')
            current_stopovers += 1
        if len(flights) > 0:
            best_flight = flights[0]
            print(best_flight)

            num_stopovers, so_out, so_in = extract_stopovers(best_flight)

            flight_info = {
                "price": best_flight["price"] ,
                "departure_city_name":best_flight["cityFrom"] ,
                "departure_airport_iata_code":best_flight["cityCodeFrom"] ,
                "arrival_city_name":best_flight["cityTo"] ,
                "arrival_airport_iata_code":best_flight["cityCodeTo"] ,
                "outbound_date":str(best_flight["route"][0]["local_departure"]).split("T")[0] ,
                "inbound_date":str(best_flight["route"][-1]["local_departure"]).split("T")[0] ,
                "num_stopovers": num_stopovers, # tuple(stopoveroutbound, stopoversin inbound)
                "stopovers_out": so_out, # lista kodow
                "stopovers_in": so_in #lista kodow
            }
            print(flight_info)
            
            for row in user_info:
                
                user_phone_number = row["phoneNumber"]
                twilio_manager.send_SMS(flight_info=flight_info, phone_number=user_phone_number)


if __name__=="__main__":
    main()