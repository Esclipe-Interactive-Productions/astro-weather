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
    global activedescription, citylabel, temperaturelabel, feelslikelabel, windspeedlabel
    citylabel = l(app, text=str(weatherdata["city"]), font=("Times", 18))
    citylabel.place(x=10, y=50)
    temperaturelabel = l(app, text=str(weatherdata["temperature"]) + ("°F"), font=("Times", 14))
    temperaturelabel.place(x=10, y=70)
    feelslikelabel = l(app, text=("Feels like ") + str(weatherdata["feels_like"]) + ("°F"), font=("Times", 14))
    feelslikelabel.place(x=10, y=250)
    windspeedlabel = l(app, text=("Wind speed is ") + str(weatherdata["wind_speed"]) + (" mph"), font=("Times", 14))
    windspeedlabel.place(x=10, y=270)
    activedescription = True
    print("Weather descriptions added.")
    return weatherdata

def weatherdescriptiondel():
    global activedescription
    if activedescription == True:
        citylabel.destroy()
        temperaturelabel.destroy()
        feelslikelabel.destroy()
        windspeedlabel.destroy()
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
versiontitle = l(app, text="ver. 0.5.49", font=("Times", 12))
# format: major.minor.build.revision
versiontitle.place(x=550, y=450)
searchentry = e(app, width=160, font=("Times", 11), placeholder_text="insert city name")
searchentry.place(x=100, y=5)
searchbutton = b(app, text="search", font=("Times", 11), width=55, fg_color="green", hover_color="dark green", command=searchcity)
searchbutton.place(x=275, y=5)
settingsbutton = b(app, text="settings", font=("Times", 11), fg_color="green", hover_color="dark green", width=70)
settingsbutton.place(x=550, y=5)

app.mainloop()
