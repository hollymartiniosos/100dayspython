import requests
from datetime import datetime as dt
import time
import pytz
#import smtplib

MY_LAT = -27 # Your latitude
MY_LONG = 153 # Your longitude
#MY_EMAIL = "gsdgs@gmail.com"
#MY_PASSWORD = ""

#Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
   
    #If the ISS is close to my current position
    if abs(MY_LONG - iss_longitude) < 5 and abs(MY_LAT - iss_latitude) < 5:
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = dt.fromisoformat(data["results"]["sunrise"])  
    sunset = dt.fromisoformat(data["results"]["sunset"])    

    time_now = dt.now(tz=pytz.UTC)

    if time_now < sunrise or time_now > sunset:
        print("Look up")# Then send me an email to tell me to look up.
        return True
       

while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        print("Look Up")
     
        #Send email
        #connection = smtplib.SMTP("smtp.gmail.com")
        #connection.starttls()
        #connection.login(MY_EMAIL, MY_PASSWORD)
        #connection.sendmail(
        # from_addr=MY_EMAIL,
        # to_addr=MY_EMAIL,
        # msg= "Subject: Look Up\n\nThe ISS is above you in the sky."
        # )
    else:
        print("Not in range")   


