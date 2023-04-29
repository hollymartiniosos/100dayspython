from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

print(os.environ.items())
FB_USERNAME = os.environ["FB_USER"]
FB_PASSWORD = os.environ["FB_PASS"]
chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"

ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get(r'https://tinder.com/')
driver.maximize_window()
time.sleep(2)
log_in_button = driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in_button.click()
time.sleep(2)
log_w_fb = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
log_w_fb.click()
time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
username_fb = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')

username_fb.send_keys(FB_USERNAME)
pass_fb = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
pass_fb.send_keys(FB_PASSWORD)
log_in_fb_button= driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
log_in_fb_button.click()
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)
allow_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_button.click()
time.sleep(1)
not_intrested_button=driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
not_intrested_button.click()
time.sleep(1)
cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()
time.sleep(10)

for _ in range(50):
    try:
        nope_button = driver.find_element(By.CSS_SELECTOR, '#s-407411262 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-nope-default\) > button > span > span')
        nope_button.click()
        time.sleep(5)
        print(f"done {_+1} times")
    except:
        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]').click()    
        time.sleep(3)

driver.quit()