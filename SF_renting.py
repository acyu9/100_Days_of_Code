import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


ZILLOW_LINK = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.85923291322895%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.691255580355254%2C%22west%22%3A-122.56825534228516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSd0dFlUrgnGs-DS-rard65iGcvDNOc2Uoi5Md1ldiZuNYe75g/viewform?usp=sf_link"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Get and save raw html text with Beautiful Soup
response = requests.get(url=ZILLOW_LINK, headers=header)
response.raise_for_status()
text = response.text
soup = BeautifulSoup(text, "html.parser")

# Only returns the first 9 prices
raw_prices = soup.find_all(attrs={"data-test": "property-card-price"})
prices = [price.text.split("+")[0].split("/")[0] for price in raw_prices]
#print(prices)

# Addresses
raw_addresses = soup.find_all(attrs={"data-test": "property-card-addr"})
addresses = [address.text for address in raw_addresses]
#print(addresses)

# Links
raw_links = soup.find_all(attrs={"data-test": "property-card-link"})
links = []
for link in raw_links:
    href = link.get("href")
    if "http" in href:
        links.append(href)
    else:
        links.append(f"https://www.zillow.com{href}")
#print(links)

# Set up Selenium
chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(GOOGLE_FORM_LINK)
sleep(3)

# Input info
for i in range(len(prices)):
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[i])
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[i])
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links[i])

    # Submit form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    # Click to submit another form
    another_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_button.click()
    