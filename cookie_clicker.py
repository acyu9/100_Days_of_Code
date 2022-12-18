import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Chromedriver\chromedriver.exe"
# Use an instance of Service class to avoid DeprecationWarning
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Gather the costs of items in store
stores = driver.find_elements(By.CSS_SELECTOR, "#store div")
# Removes the last element, empty string, from the list
stores = stores[:-1]
costs = []
items = []
for store in stores:
    # Isolate the cost of the item and put into a list. Int can't use , so change to ""
    cost = int(store.find_element(By.CSS_SELECTOR, "b").text.split("- ")[-1].replace(",", ""))
    itemID = store.find_element(By.CSS_SELECTOR, "b").text.split(" -")[0]
    items.append(itemID)
    costs.append(cost)

# Dictionary of itemIDs and prices
dictionary = {"buy"+item:cost for (item, cost) in zip(items, costs)}

# reverse() reverses in place, but does not return the array. Can only reverse list
reversed_dict = dict(reversed(list(dictionary.items())))

# Compare current time to current time + 5 sec
timeout = time.time() + 5
end_game = time.time() + 60*5
continue_game = True

while continue_game: 
    cookie = driver.find_element(By.ID, "cookie").click()

    if time.time() > timeout:
        timeout = time.time() + 5
        try:    
            money = int(driver.find_element(By.ID, "money").text)
        except ValueError:
            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        # Compare money to cost starting with the most expensive item
        for item in reversed_dict:
            if money > reversed_dict[item]:
                driver.find_element(By.ID, f"{item}").click()
                break

    # Run the game for 5 minutes     
    if time.time() > end_game:
        cookies_sec = driver.find_element(By.ID, "cps")
        print(cookies_sec.text)
        continue_game = False
        driver.quit()
