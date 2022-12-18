import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B07VRGK6NY/ref=sbl_dpx_kitchen-electric-cookware_B0B8F38J2B_0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6"
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, "lxml")

# Select returns all html after this class
# Find returns <span class="a-offscreen">$62.96</span>
# Sometimes shows None, sometimes show the price and name...
# Amazon site is checking if you are a bot.  If you print(response.text), you will see the message.
print(response.text)
price = float(soup.find(name="span", class_="a-offscreen").get_text().split("$")[1])
title = soup.find(name="span", id="productTitle").get_text().strip()

BUY_PRICE = 50

# Send email alert about low price
if price < BUY_PRICE:
    message = f"{title} is now {price}!"

    with smtplib.SMTP("address", port=587) as connection:
        connection.starttls()
        result = connection.login("email", "password")
        connection.sendmail(
            from_addr="sample@email.com",
            to_addr="sample2@email.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )