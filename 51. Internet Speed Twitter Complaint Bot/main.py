from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os


chrome_driver_path = r"C:/Users/Martyna/projects/100dayspython/Selenium driver to chrome/chromedriver.exe"
TWITTER_USERNAME = os.environ["TWITTER_USER"]
TWITTER_PASSWORD = os.environ["TWITER_PASS"]
PROMISED_DOWN = 100
PROMISED_UP = 10

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        ser = Service(executable_path = driver_path)
        op = wb.ChromeOptions()
        op.add_experimental_option("detach", True)
        self.driver = wb.Chrome(service=ser, options=op)
        self.down = 0
        self.up = 0
        self.should_tweet = False

    

    def get_internet_speed(self): 
        self.driver.get(r'https://www.speedtest.net/')
        self.driver.maximize_window()
        time.sleep(2)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(100)
        down_find = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span')
        self.down = float(down_find.text)
        up_find = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(up_find.text)

        if self.down < PROMISED_DOWN: 
            self.should_tweet= True
            print('only down is lower')      
        elif self.up < PROMISED_UP:
            self.should_tweet= True
            print('only up is lower')
        else:    
            print("all ok") 

        return(self.should_tweet, self.up, self.down)
    

    def tweet_at_provider(self):
        self.driver.get(r'https://twitter.com/home')
        self.driver.maximize_window()
        time.sleep(4)
        twitter_login_username = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        twitter_login_username.send_keys(TWITTER_USERNAME)
        twitter_login_username.send_keys(Keys.ENTER)
        time.sleep(4)

        try:
            twitter_login_pass = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            twitter_login_pass.send_keys(TWITTER_PASSWORD)
            twitter_login_pass.send_keys(Keys.ENTER)
        except:
            twitter_verify_username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            twitter_verify_username.send_keys("kpefot")
            twitter_verify_username.send_keys(Keys.ENTER)
            time.sleep(2)
            twitter_verify_pass = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            twitter_verify_pass.send_keys(TWITTER_PASSWORD)
            twitter_verify_pass.send_keys(Keys.ENTER)

        time.sleep(5)
        message_box = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div') 
        message_box.send_keys(f'Hey Internet Provider, why my internet speed is only {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?')
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span')
        time.sleep(4)
        tweet_button.click()
  


bot = InternetSpeedTwitterBot(driver_path=chrome_driver_path)
bot.get_internet_speed()
print(bot.should_tweet)
if bot.should_tweet == True:
    bot.tweet_at_provider()
    print('tweeted')
else:
    print('all ok') 

# bot.tweet_at_provider()
# print('tweeted')    