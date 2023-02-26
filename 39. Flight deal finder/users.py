import os
import requests 

SHEETY_API = "https://api.sheety.co/d2dd5f6e5713c07f78a8b0452cbb68a8/flightDeals/users/"
SHEETY_TOKEN = os.environ["SHEETY_PRICES_TOKEN"]

class User:

    def add_user(self) -> None:
        bearer_headers = {
            "Authorization": f'Bearer {SHEETY_TOKEN}' 
            }
        params = {
            "user": {
                "firstName" : str(input("Welcome to Flight Club. \nWe find the best flight deals and text you. \nWhat is your first name?")),
                "lastName": str(input("What is your last name?")),
                "phoneNumber": int(input("What is your phone number?"))
                }
            }

        response = requests.post(f'{SHEETY_API}', headers=bearer_headers, json=params)
        if response.status_code == 200:
            print("You're in the club!")
            
        else:
            print(f'Failed {response.json()}') 

    def users_info(self) -> list:
        bearer_headers = {
            "Authorization": f'Bearer {SHEETY_TOKEN}' 
        }

        response = requests.get(SHEETY_API, headers=bearer_headers)
        if response.status_code == 200:
            print("Successfully fetched the data")
            sheety_users = response.json()
            users_info = sheety_users["users"]
            print(users_info)
            return users_info
        else:
            print(f'Failed {response.status_code}') 
            return []        

if __name__ == "__main__":
    cos4 = User()
    cos4.add_user()   
    cos4.users_info()    