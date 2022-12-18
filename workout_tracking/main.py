import requests
from datetime import datetime
import os

#APP_ID = "ab765dec"
APP_ID = os.environ.get("APP_ID")
API_KEY = "b2b4dde7f87d694671f3857ce519bd60"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/1bdfa015b44ff2d26b8c4f712b9bd62a/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameter = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=ENDPOINT, json=parameter, headers=headers)
result = response.json()

bearer = {
    "authorization": "Bearer Bearer"
}

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().time().isoformat("seconds")

# Add row to Google Sheet via Sheety
for exercise in result["exercises"]:
    parameters = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=parameters, headers=bearer)
    print(sheety_response.text)

