import requests
from bs4 import BeautifulSoup
import lxml
from twilio.rest import Client
import os

URL = r"https://www.amazon.com.au/XGIMI-Portable-Projector-Android-Bluetooth/dp/B09KC3S1V6/ref=sr_1_3?crid=3GE1ENZFU4RMB&keywords=nebula%2Bcapsule%2B3&qid=1681609421&sprefix=nebula%2Bca%2Caps%2C1009&sr=8-3&th=1"

headers= {
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site":"cross-site",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9,pl;q=0.8",
    'x-https':'on',
    
}

response = requests.get(URL, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
price_text = soup.find(name="span", class_="a-price-whole").getText()
price_number = float(price_text.replace(",",""))
# print(price_number)
# price_number = 1498.0
target_price = 1500.00
if price_number <= target_price:
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone = os.environ['TWILIO_PHONE_NUMBER']
    my_phone_number = os.environ['MY_PHONE_NUMBER']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body="AMAZON PRICE ALERT! The projector you wanted is now on special!",
                                from_=twilio_phone,
                                to= my_phone_number
                            )
    print(message.status)

