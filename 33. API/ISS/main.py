import requests
import time
import json

def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    timestamp = data["timestamp"]
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    iss_position = (latitude,longitude)
    return iss_position, timestamp

records = []
count = 0 
while True:
    time.sleep(10)
    count += 1
    print(f"hitting API {count}, {time.time()}")
    iss_position, timestamp = check_position()    
    records.append({"time": timestamp, "position": iss_position})
    with open("iss_vis2.json", "w") as data_file:
        json.dump(records, data_file, indent=4)
