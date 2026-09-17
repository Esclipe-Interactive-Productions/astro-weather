import json

with open("data/settings.json", "r") as file:
    settings = json.load(file)
    theme = settings["theme"]
    temperatureunit = settings["temperature unit"]
    speedunit = settings["speed unit"]
    pressureunit = settings["pressure unit"]
    distanceunit = settings["distance unit"]
    savesearches = settings["save searches"]
    nofications = settings["notifcations"]
    weatheralerts = settings["weather alerts"]
