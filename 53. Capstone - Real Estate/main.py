from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time


FORM = r"https://docs.google.com/forms/d/e/1FAIpQLSeoaFNHJR5cjbkosgQoABHY7wmdlRgk8TEx06lE94WG6nhM8A/viewform?usp=sf_link"
#BS
URL = r'https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.35439760009766%2C%22east%22%3A-118.19475251953125%2C%22south%22%3A33.98435454890345%2C%22north%22%3A34.100140241917195%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22min%22%3A2400%2C%22max%22%3A2800%7D%2C%22price%22%3A%7B%22min%22%3A485748%2C%22max%22%3A566706%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D'
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

req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
all_elements = soup.select('div .result-list-container ul div .property-card-data')
all_links = []
all_prices = []
all_addresses = []

for url in all_elements: 
    for link in url.find_all('a', class_='property-card-link'):
        all_links.append(link["href"])

for url in all_elements:
    for unit_price in url.find_all(attrs={"data-test":"property-card-price"}):
        price = unit_price.text
        price_value = price.replace("$","").replace(",","").replace("/mo","")
        all_prices.append(price_value)

for url in all_elements:
    for unit_address in url.find_all(attrs={"data-test":"property-card-addr"}):
        address = unit_address.text
        all_addresses.append(address)    

print(all_links)
print(all_prices)  
print(all_addresses)        


#SELENIUM
chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"
ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get(FORM)
driver.maximize_window()
time.sleep(5)
for i in range(len(all_addresses)):
    address_in_form = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_in_form.send_keys(all_addresses[i])
    price_in_form = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_in_form.send_keys(all_prices[i])
    link_in_form = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_in_form.send_keys(all_links[i])
    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
    time.sleep(3)
    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(3)
