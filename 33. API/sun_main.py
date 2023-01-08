import requests
from datetime import datetime as dt
import pytz

params= {"lat":-27, "lng":153, "formatted":0 }
response = requests.get(url="http://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data= response.json()
print(data)
sunrise = data["results"]["sunrise"]  
sunset = data["results"]["sunset"]    
sunrise_dt = dt.fromisoformat(sunrise)
sunset_dt = dt.fromisoformat(sunset)


print(sunrise_dt, sunset_dt)
current_time = dt.now(tz=pytz.UTC)
print(current_time)