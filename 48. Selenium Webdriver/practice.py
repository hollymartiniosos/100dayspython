from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"
ser = Service(chrome_driver_path)
op = wb.ChromeOptions()
driver = wb.Chrome(service=ser, options=op)
driver.get('https://www.python.org/')
# times = []
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# for time in event_times:
#     times.append(time.text)

# names =[]
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# for name in event_names:
#     names.append(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)
driver.close()
driver.quit()