from dotenv import load_dotenv
from ui.settings import temperatureunit
import os
import requests

load_dotenv()

if temperatureunit == "fahrenheit" or "f":
    temperatureunit2 = "imperial"

def searchcity(cityname):
    print(cityname)
    weatherapikey = os.getenv("weatherapikey")
    response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": cityname,
            "appid": weatherapikey,
            "units": "temperatureunit2"
        }
    )
    data = response.json()
    print(data)
