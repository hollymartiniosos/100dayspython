from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

IG_USERNAME = os.environ["IG_USER"]
IG_PASSWORD = os.environ["IG_PASS"]
chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"

ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get(r'https://www.instagram.com/tamaki_nakajima_okinawa/')
driver.maximize_window()
time.sleep(2)
log_in_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a/button')
log_in_button.click()
time.sleep(2)
username_ig = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
username_ig.send_keys(IG_USERNAME)
pass_ig = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
pass_ig.send_keys(f'{IG_PASSWORD}*!T%7Cw5sa')
log_in_ig_button= driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')
log_in_ig_button.click()
time.sleep(5)
try:
    followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
    followers.click()
    time.sleep(5)   
    clicking = True
    count = 0 
    while clicking:
        try:    
            follow_button = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{count+1}]/div/div/div/div[3]/div/button')
            print(follow_button)
            follow_button.click()
            count += 1 
            if count == 5000:
                clicking = False
        except:
            time.sleep(7)
            follow_button = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{count+1}]/div/div/div/div[3]/div/button')
            print(follow_button)
            follow_button.click()
            count += 1  
            if count == 5000:
                clicking = False
        
except:
    save_info = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div') 
    save_info.click()  
    time.sleep(5)
    followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
    followers.click()
    time.sleep(5)
    heading = driver.find_element(By.CLASS_NAME, "_ac78")
    print(heading)
    
    clicking = True
    # IG limit is only 100 new followers a day
    count = 0 
    while clicking:
        try:    
            follow_button = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{count+1}]/div/div/div/div[3]/div/button')
            print(follow_button)
            follow_button.click()
            count += 1 
            if count == 100:
                clicking = False
        except:
            time.sleep(7)
            follow_button = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{count+1}]/div/div/div/div[3]/div/button')
            print(follow_button)
            follow_button.click()
            count += 1
            if count == 100:
                clicking = False  
        
driver.quit()        
        

    

