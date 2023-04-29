from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

LINKEDIN_USER = os.environ["LINKEDIN_USER"]
LINKEDIN_PASS = os.environ["LINKEDIN_PASS"]
chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"

ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
#to keep window open
op.add_experimental_option("detach", True)
driver = wb.Chrome(service=ser, options=op)
driver.get(r'https://www.linkedin.com/jobs/search/?currentJobId=3522232095&f_AL=true&f_E=2&f_JT=F&f_WT=2%2C3&geoId=101452733&keywords=python%20developer&location=Australia&refresh=true')
driver.maximize_window()
sign_in_button = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()
email = driver.find_element(By.ID, "username")
email.send_keys(LINKEDIN_USER)
password = driver.find_element(By.ID, "password")
password.send_keys(LINKEDIN_PASS)
button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
button.click()
time.sleep(5)
link_job_offers = driver.find_elements(By.CLASS_NAME, "job-card-container__company-name")
time.sleep(5)
#clicking on the object 
for job_offer in link_job_offers:
    job_offer.click()
    time.sleep(5)
    easy_apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button--top-card')
    easy_apply_button.click()
    time.sleep(5)
    phone_number = driver.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3556021694-86363579-phoneNumber-nationalNumber")
    phone_number.send_keys("0222333666")
    next_button = driver.find_element(By.XPATH, "//*[text()='Next']")
    next_button.click()
    #doesn't work
    # upload = driver.find_element(By.XPATH, "//*[text()='Upload resume']")
    # upload.click()
    # upload.send_keys("C:/Users/Martyna/projects/100dayspython/49. Job Applications LinkedIn/dvz.pdf")
    # upload.send_keys("ENTER")

    
print('done')