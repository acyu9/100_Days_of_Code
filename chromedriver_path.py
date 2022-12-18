from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
# Use an instance of Service class to avoid DeprecationWarning
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_2?crid=323OR5VRKALKB&keywords=instant+pot&qid=1667492577&qu=eyJxc2MiOiI0LjU1IiwicXNhIjoiNC4xNSIsInFzcCI6IjMuNjcifQ%3D%3D&sprefix=instant+pot%2Caps%2C170&sr=8-2")
# Outputs $79 99 in two separate lines for some reason
info = driver.find_element(By.CLASS_NAME, "a-price")
# Combines back to $79.99 and changes web element to string
price = info.text.replace("\n", ".")
print(price)




# Closes a single/active tab
#driver.close()
# Quits entire browser
driver.quit()