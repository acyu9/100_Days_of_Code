import requests
from datetime import datetime

TOKEN = "generateownkey"
USERNAME = "username123"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create account (only need to run once)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Habit Tracker",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Header makes the token more secure instead of being part of the url
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime.now()

pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/20221015"
update_config = {
    "quantity": "25"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)