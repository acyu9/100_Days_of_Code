from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
# Use an instance of Service class to avoid DeprecationWarning
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

# Find the lists of events via XPath
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# Put the time and location in lists of webelements
days = events.find_elements(By.TAG_NAME, "time")
names = events.find_elements(By.TAG_NAME, "a")
# Dictionary comprehension to tap in individual element in the lists and save as string via .text
dictionary = {i: {"time": days[i].text, "name": names[i].text} for i in range(len(days))}
print(dictionary)

driver.quit()