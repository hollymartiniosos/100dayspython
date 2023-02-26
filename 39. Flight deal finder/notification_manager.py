import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.


    def send_SMS(self, flight_info: dict, phone_number) -> None:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        twilio_phone = os.environ['TWILIO_PHONE_NUMBER']

        notification_message = f"""
           Low price alert! Only AUD{flight_info["price"]} to fly from 
           {flight_info["departure_city_name"]}-{flight_info["departure_airport_iata_code"]} 
           to {flight_info["arrival_city_name"]}-{flight_info["arrival_airport_iata_code"]}, 
           from {flight_info["outbound_date"]} to {flight_info["inbound_date"]}.
           Flights out have {flight_info["num_stopovers"][0]} stopovers, via {", ".join(flight_info["stopovers_out"])}.
           Flights in have {flight_info["num_stopovers"][1]} stopovers, via {", ".join(flight_info["stopovers_in"])}.  
        """

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= notification_message,
            from_=twilio_phone,
            to=phone_number
                        )
        print(message.status)
    