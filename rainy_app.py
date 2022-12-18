import requests
import os

# Use environment variable to hide authen key
parameters = {
    "lat": 34.052235, 
    "lon": -118.243683, 
    "appid": os.environ.get("appid"),
    "exclude": "current,minutely,daily",
}
#"appid": "69f04e4613056b159c2761a9d9e664d2"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data)

# list of the hourly forecasts weather ID for 12 hours

# Method 1: for loop
# weathers = []
# for i in range(12):
#     weathers.append(weather_data["hourly"][i]["weather"][0]["id"])
# print(weathers)


# Method 2: list comprehension
weathers = ["True" for hour in range(12) if (weather_data["hourly"][hour]["weather"][0]["id"]) < 700]
if len(weathers) > 0:
    print("Bring an umbrella.")
else:
    print("No rain.")


# Method 3: slice notation and any (checks if there's at lest one True)
# a[start:stop] items start through stop-1
# weather_slice = weather_data["hourly"][:12]
# if any(i["weather"][0]["id"] < 700 for i in weather_slice):
#    print("rain")