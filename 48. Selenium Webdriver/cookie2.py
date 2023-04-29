from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"

ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")

timeout = time.time() + 5
play_time = time.time() + 60 * 5
while time.time() < play_time:
    cookie.click()

    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")

        if len(items) > 0:
            items[-1].click()

        timeout = time.time() + 5

print("Your final score:", driver.find_element(By.ID, "cps").text)