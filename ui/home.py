import customtkinter as ctk
from ui.settings import theme
from weatherapi import searchcity as getweather

b = ctk.CTkButton
l = ctk.CTkLabel
e = ctk.CTkEntry

ctk.set_appearance_mode(theme)

weatherdata = None

def weatherdescription():
    print(weatherdata["temperature"])
    descriptionlabel = l(app, text=(weatherdata["temperature"]) + str("°F"), font=("Times", 14))
    descriptionlabel.place(x=320, y=70)
    return weatherdata

def searchcity():
    cityname = searchentry.get()
    print(cityname)
    global weatherdata
    weatherdata = getweather(cityname)
    weatherdescription()

app = ctk.CTk()
app.geometry("640x480")
app.title("astro weather")
app.resizable(False, False)

maintitle = l(app, text="astro weather", font=("Times", 15))
maintitle.place(x=10, y=5)
searchentry = e(app, width=160, font=("Times", 11), placeholder_text="insert city name")
searchentry.place(x=100, y=5)
searchbutton = b(app, text="search", font=("Times", 11), width=55, fg_color="green", hover_color="dark green", command=searchcity)
searchbutton.place(x=275, y=5)
settingsbutton = b(app, text="settings", font=("Times", 11), fg_color="green", hover_color="dark green", width=70)
settingsbutton.place(x=550, y=5)

app.mainloop()
