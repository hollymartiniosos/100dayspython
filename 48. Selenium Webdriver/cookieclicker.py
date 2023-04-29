from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt, timedelta
import time
from threading import Thread

chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"
NUM_THREADS = 5
ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")
cookie_total = driver.find_element(By.ID, "money")
cookies_rate = driver.find_element(By.ID, "cps")

store = driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1][::-1]
print(len(store))




def cost_check(store_item, separator):
    # upgrades = []
    # for i in store:
        
        upgrade = store_item.text
        upgrade_split = upgrade.split(separator)
        cost = upgrade_split[1].replace(',','')
        return float(cost)
        # print(cost)
    #     upgrades.append(int(cost))
    # upgrade_costs = upgrades[::-1]
    # return upgrade_costs
    # print(upgrade_costs)

def clickcookie():
    cookie.click()


# for n in range(10):
#     clickcookie()
# print(cookie_total.text, cookies_rate.text)    

current_time = dt.now()
end_time = current_time + timedelta(minutes=5)
check_time = current_time + timedelta(seconds=5)
# print(current_time, end_time, check_time)

while end_time > current_time:
    

    while current_time <= check_time:
        
        clickcookie()
        current_time = dt.now()
    check_time = check_time + timedelta(seconds=5)
    cookie_total_value = int(cookie_total.text.replace(",",""))
    # cookies_rate_value= cost_check(cookies_rate, ":")
    # costs = cost_check()
    prices = [cost_check(obj, "-") for obj in store if cost_check(obj, "-")]
    can_afford = [price <= cookie_total_value for price in prices]
    
    # while cookie_total_value>=cookies_rate_value and any(can_afford):
         #kup najdrozszy upgrade
    print(8-can_afford.index(True))     
    store[can_afford.index(True)].click()
        # cookie_total_value = int(cookie_total.text.replace(",",""))
        # cookies_rate_value= cost_check(cookies_rate, ":")
    time.sleep(0.1)
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1][::-1]
        # prices = [cost_check(obj, "-") for obj in store]
        # can_afford = [price <= cookie_total_value for price in prices]
        # print(any(can_afford))
    
    current_time = dt.now()

print(cost_check(cookies_rate, ":")) 
