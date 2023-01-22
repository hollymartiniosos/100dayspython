import requests as r
from datetime import datetime as dt
import os

TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = os.environ["PIXELA_USERNAME"]


# Step 1. Create a new user via post request
# instruction from documentation
# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}


pixela_domain = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}


# response = r.post(url = pixela_domain, json = user_params)
# print(response.text)


# Step 2. Create a graph definition
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu","timezone":"Asia/Tokyo","isSecret":true,"publishOptionalData":true}'
# {"message":"Success.","isSuccess":true}

graph_endpoint = f"{pixela_domain}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "KM",
    "type": "float",
    "color": "momiji",
    "timezone": "Australia/Brisbane"    
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = r.post(url = graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

#Step 3. Create a pixel and put it on the graph
pixel_endpoint = f"{pixela_domain}/{USERNAME}/graphs/graph1"

print(dt.now())
today = dt.now().strftime("%Y%m%d")
yesterday = dt(year=2023, month=1, day = 21).strftime("%Y%m%d")

pixel_params = {
    "date": yesterday,
    "quantity": "25"
}

response = r.post(url = pixel_endpoint, json=pixel_params, headers=headers)
print(response.text) 

#Step 4. Update the pixel
update_pixel_endpoint = f"{pixela_domain}/{USERNAME}/graphs/graph1/{yesterday}"

update_pixel_params = {
    "quantity": "30"
}

# response = r.put(url = update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text) 

#Step 5. Delete a pixel

# response = r.delete(url = update_pixel_endpoint, headers=headers)
# print(response.text) 