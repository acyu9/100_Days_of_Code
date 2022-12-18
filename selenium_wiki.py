from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
# Use an instance of Service class to avoid DeprecationWarning
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # Find the id and then the first anchor tag
# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# #count.click()

# # Easier way to find and click on link
# #all_portals = driver.find_element(By.LINK_TEXT, "View source").click()

# # Automatically type in search bar then enter/submit
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("John")
last_name = driver.find_element(By.NAME, "lName").send_keys("Smith")
email = driver.find_element(By.NAME, "email").send_keys("example@email.com")
button = driver.find_element(By.CSS_SELECTOR, "button").submit()


