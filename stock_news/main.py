import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "N4HYOM33Z6NTYBTO"
NEWS_API_KEY = "a409fdaacc6e47bbb6f674a94b78e4cc"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    #"apikey": os.environ.get("apikey"),
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Change dict to list and save only stock values, not date key
data_list = [value for (key, value) in data.items()]
yesterday_close = float(data_list[0]["4. close"])
two_days_close = float(data_list[1]["4. close"])
percentage = abs((yesterday_close - two_days_close) / two_days_close * 100)
print(percentage)

if percentage > 5:
    print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "language": "en",
    "q": COMPANY_NAME,
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

news_articles = news_data["articles"]
if len(news_articles) > 3:
    three_articles = news_articles[:3]
    print(three_articles)
else:
    print(news_articles)

#articles = [news_data["articles"][i] for i in range(3)]
#print(articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
# for article in formatted_articles:
#     message = client.message.create(
#         body = article,
#         from = "number",
#         to = "number",
#     )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

