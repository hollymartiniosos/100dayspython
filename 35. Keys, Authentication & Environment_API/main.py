import requests
import os
from twilio.rest import Client




#1 My Idea with OpenMeteo

# API for OpenMeteo for BNE, AU location in BNE time zone
api_OM = "https://api.open-meteo.com/v1/forecast?latitude=-27.15&longitude=153&hourly=precipitation&timezone=Australia%2FBrisbane"

def get_data(api):
    response= requests.get(f"{api}")
    if response.status_code == 200:
        print("Successfully fetched the data")
        forecast = response.json()
        # print(forecast)
        return forecast
    else:
        print(f'Failed {response.status_code}')    

 
def checking_if_rain(data):
    precipitation = data["hourly"]["precipitation"]
    # print(f"YEP {precipitation}")
    for i in precipitation[8:21]:
        if i >= 0.2:
            # send_SMS("It's gonna rain. Take your umbrella today!", numer)
            print("It's gonna rain. Take your umbrella today!")
            send_SMS("It's gonna rain. Take your umbrella today!", "xxxxxxxxxx")
            return
         
# Keys saved in my env 
def send_SMS(text:str , phone_number:str) -> None:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone = os.environ['TWILIO_PHONE_NUMBER']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body=text,
                                from_=twilio_phone,
                                to=phone_number
                            )
    print(message.status)
    
def main():
    weather_data = get_data(api_OM)
    checking_if_rain(weather_data)
    
    
if __name__== "__main__":
    main()    


#course with OpenWeather - you need to buy subscription for this to work - api_key not valid

# OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
# api_key = "key"

# weather_params = {
#     "lat": -27.15,
#     "lon": 153,
#     "appid": api_key,
#     "exclude": "current,minutely,daily" 
# }

# response = requests.get(OWM_Endpoint, params=weather_params)
#response.raise_for_status()
#weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]

# will_rain = False

# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True

# if will_rain:
#     print("Bring umbrella")        