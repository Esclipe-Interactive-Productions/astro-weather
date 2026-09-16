from dotenv import load_dotenv
import os
import requests

load_dotenv()

def searchcity(cityname):
    print(cityname)
    weatherapikey = os.getenv("weatherapikey")
    response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": cityname,
            "appid": weatherapikey,
            "units": "imperial"
        }
    )
    data = response.json()
    print(data)
