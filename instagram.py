from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
service = Service(chrome_driver_path)
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "username"
PASSWORD = "password"


class InstaFollower:
    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        # Need to load first or else get NoSuchElementException
        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        sleep(10)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)

        # Modal is a popup window that is displayed on top of the current page
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for _ in range(10):
            # Scroll the top of the modal by the height of the modal
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta = InstaFollower(service)
insta.login()
insta.find_followers()
insta.follow()
