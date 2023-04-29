from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"

ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
#to keep window open
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get('https://jbzd.com.pl/')
driver.maximize_window()

rejestracja = driver.find_element(By.XPATH, '//*[@id="user-sign-box"]/div[1]/form/div[5]/a[2]')
#clicking on the object 
rejestracja.click()

name = driver.find_element(By.XPATH, '//*[@id="login"]')
name.send_keys("")
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("")
pass_1 = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_1.send_keys("")
pass_2 = driver.find_element(By.XPATH, '//*[@id="password_confirmation"]')
pass_2.send_keys("")
button = driver.find_element(By.XPATH, '//*[@id="rules"]')
button.click()
potwierdzenie = driver.find_element(By.XPATH, '//*[@id="user-sign-box"]/div[1]/form/div[8]/div/button')
potwierdzenie.click()