from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 50
PROMISED_UP = 10
TWITTER_EMAIL = "sample@email.com"
TWITTER_PASSWORD = "password"

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
# Use an instance of Service class to avoid DeprecationWarning
service = Service(chrome_driver_path)


class InternetSpeedTwitterBot():
    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        self.go_button.click()
        sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        #print(upload_speed.text)
        self.driver.quit()

    def tweet_at_provider(self):
        # login to twitter
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(5)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        
        # compose message
        sleep(5)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, ".DraftEditor-editorContainer div")
        tweet = f"Hey, why is my internet speed {self.down}/{self.up} when I pay for {PROMISED_DOWN}/{PROMISED_UP}?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        # send message
        tweet_button = self.driver.find_element(By.XPATH, "path")
        tweet_button.click()
        sleep(2)
       
        self.driver.quit()


bot = InternetSpeedTwitterBot(service)
bot.get_internet_speed()
bot.tweet_at_provider()
