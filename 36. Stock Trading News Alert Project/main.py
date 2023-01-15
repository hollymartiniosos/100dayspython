import os
import requests
import json
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TARGET_PHONE_NUMBER = "xxxxxxx"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_data():
    alpha_stock_api_key = os.environ['ALPHA_STOCK_API_KEY']
    alpha_stock_api = "https://www.alphavantage.co/query"
    stock_api_params = {
        "function":"TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": alpha_stock_api_key 
    } 

    response = requests.get(alpha_stock_api, params=stock_api_params)

    if response.status_code == 200:
        print("Successfully fetched the data")
        stock_data = response.json()
        return stock_data
    else:
        print(f'Failed {response.status_code}')   

def get_news():
    news_api_key = os.environ['NEWS_API_KEY']
    news_api = "https://newsapi.org/v2/everything"
    news_api_params = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "pageSize": 3,
        "language": "en",
        "apikey": news_api_key 
    } 

    response = requests.get(news_api, params=news_api_params)

    if response.status_code == 200:
        print("Successfully fetched the data")
        news_data = response.json()             
        return news_data
    else:
        print(f'Failed {response.status_code}') 


def send_SMS(percentage) -> None:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone = os.environ['TWILIO_PHONE_NUMBER']

    sign = '🔺' if percentage > 0 else '🔻'

    news_data = get_news()

    client = Client(account_sid, auth_token)
    for i in range(0,3):
        message = client.messages.create(
                                body=(f'{STOCK}: {sign}{round(percentage*100)}% \n Headline: {news_data["articles"][i]["title"]} \n Brief: {news_data["articles"][i]["description"]}'),
                                from_=twilio_phone,
                                to=TARGET_PHONE_NUMBER
                            )
        print(message.status)

    
            

def analyse_data(data):
    last_day, second_last_day = sorted(data["Time Series (Daily)"], reverse=True)[:2]
    closing_value_today = float(data["Time Series (Daily)"][last_day]["4. close"]) 
    closing_value_yesterday = float(data["Time Series (Daily)"][second_last_day]["4. close"])   
    percentage = closing_value_today/closing_value_yesterday - 1
    
    if abs(percentage) > 0.05:
    
       send_SMS(percentage)
    else:
        print(f'No notification, only {round(percentage*100)}% change.')
       
def main():
    stock_data = get_stock_data()
    # with open("stock_data.json",'w') as file:
    #     json.dump(stock_data, file)
    # with open("stock_data.json") as file:
    #     stock_data = json.load(file)
    
    analyse_data(stock_data)
    
    

if __name__== "__main__":
    main() 

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
 
         

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

