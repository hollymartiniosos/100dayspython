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
driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.maximize_window()

# number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#clicking on the object 
# number.click()

# link = driver.find_element(By.LINK_TEXT, 'Wikisource')
# link.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.close()
# driver.quit()