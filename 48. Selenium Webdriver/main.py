from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"
ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
driver = wb.Chrome(service=ser, options=op)
driver.get('https://www.amazon.com.au/XGIMI-Portable-Projector-Android-Bluetooth/dp/B09KC3S1V6/ref=sr_1_3?crid=3GE1ENZFU4RMB&keywords=nebula%2Bcapsule%2B3&qid=1681609421&sprefix=nebula%2Bca%2Caps%2C1009&sr=8-3&th=1')
price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
print(price.text)

# closing one tab 
driver.close()

# closing entire browser
driver.quit()
