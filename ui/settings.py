import json

with open("data/settings.json", "r") as file:
    settings = json.load(file)
    theme = settings["theme"]
