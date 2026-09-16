import os
import requests
from dotenv import load_dotenv

load_dotenv()

weatherapikey = os.getenv("weatherapikey")

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={
        "q": "New York",
        "appid": weatherapikey,
        "units": "imperial"
    }
)

data = response.json()
