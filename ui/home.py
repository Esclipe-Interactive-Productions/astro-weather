import customtkinter as ctk
from ui.settings import theme
from weatherapi import searchcity as getweather

b = ctk.CTkButton
l = ctk.CTkLabel
e = ctk.CTkEntry

ctk.set_appearance_mode(theme)

weatherdata = None
activedescription = False
def weatherdescription():
    global activedescription, citylabel, temperaturelabel, feelslikelabel, windlabel, humiditylabel, temperaturelabeltitle, feelslikelabeltitle, windlabeltitle, humiditylabeltitle, conditionlabel, conditionlabeltitle, countrylabel, pressurelabeltitle, pressurelabel
    citylabel = l(app, text=str(weatherdata["city"]) + (","), font=("Times", 18))
    citylabel.place(x=10, y=50)
    countrylabel = l(app, text=str(weatherdata["country"]), font=("Times", 18))
    countrylabel.place(x=10, y=75)
    conditionlabeltitle = l(app, text=("Condition"), font=("Times", 14, "bold"))
    conditionlabeltitle.place(x=169, y=50)
    conditionlabel = l(app, text=str(weatherdata["condition"]), font=("Times", 14))
    conditionlabel.place(x=240, y=50)
    temperaturelabeltitle = l(app, text=("Temperature"), font=("Times", 14, "bold"))
    temperaturelabeltitle.place(x=150, y=80)
    temperaturelabel = l(app, text=str(weatherdata["temperature"]) + ("°F"), font=("Times", 14))
    temperaturelabel.place(x=240, y=80)
    feelslikelabeltitle = l(app, text=("Feels like"), font=("Times", 14, "bold"))
    feelslikelabeltitle.place(x=170, y=110)
    feelslikelabel = l(app, text=str(weatherdata["feels_like"]) + ("°F"), font=("Times", 14))
    feelslikelabel.place(x=240, y=110)
    windlabeltitle = l(app, text=("Wind"), font=("Times", 14, "bold"))
    windlabeltitle.place(x=197, y=140)
    windlabel = l(app, text=str(weatherdata["wind_speed"]) + (" mph, ") + str(weatherdata["wind_direction"]) + ("°"), font=("Times", 14))
    windlabel.place(x=240, y=140)
    humiditylabeltitle = l(app, text=("Humidity"), font=("Times", 14, "bold"))
    humiditylabeltitle.place(x=174, y=170)
    humiditylabel = l(app, text=str(weatherdata["humidity"]), font=("Times", 14))
    humiditylabel.place(x=240, y=170)
    pressurelabeltitle = l(app, text=("Pressure"), font=("Times", 14, "bold"))
    pressurelabeltitle.place(x=176, y=200)
    pressurelabel = l(app, text=str(weatherdata["pressure"]), font=("Times", 14))
    pressurelabel.place(x=240, y=200)
    activedescription = True
    print("Weather descriptions added.")
    return weatherdata

def weatherdescriptiondel():
    global activedescription
    if activedescription == True:
        citylabel.destroy(), temperaturelabel.destroy(), feelslikelabel.destroy(), windlabel.destroy(), humiditylabel.destroy(), temperaturelabeltitle.destroy(), feelslikelabeltitle.destroy(), windlabeltitle.destroy(), humiditylabeltitle.destroy(), conditionlabel.destroy(), conditionlabeltitle.destroy(), countrylabel.destroy(), pressurelabel.destroy(), pressurelabeltitle.destroy()
        activedescription = False
        print("Weather descriptions deleted.")
    weatherdescription()

def searchcity():
    cityname = searchentry.get()
    print(cityname)
    global weatherdata
    weatherdata = getweather(cityname)
    weatherdescriptiondel()

app = ctk.CTk()
app.geometry("640x480")
app.title("astro weather")
app.resizable(False, False)

maintitle = l(app, text="astro weather", font=("Times", 15))
maintitle.place(x=10, y=5)
versiontitle = l(app, text="ver. 0.5.50", font=("Times", 12))
# format: major.minor.build.revision
versiontitle.place(x=550, y=450)
searchentry = e(app, width=160, font=("Times", 11), placeholder_text="insert city name")
searchentry.place(x=100, y=5)
searchbutton = b(app, text="search", font=("Times", 11), width=55, fg_color="green", hover_color="dark green", command=searchcity)
searchbutton.place(x=275, y=5)
settingsbutton = b(app, text="settings", font=("Times", 11), fg_color="green", hover_color="dark green", width=70)
settingsbutton.place(x=550, y=5)

app.mainloop()
