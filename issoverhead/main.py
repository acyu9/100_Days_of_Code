import requests
from datetime import datetime, timezone
from time import sleep

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    lat_range = (MY_LAT-5, MY_LAT+5)
    long_range = (MY_LONG-5, MY_LONG+5)
    if iss_latitude in lat_range and iss_longitude in long_range:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    #run the code every 60 seconds.
    sleep(60)
    #If the ISS is close to my current position and it is currently dark
    if iss_overhead() and is_night():
        print("send email")
