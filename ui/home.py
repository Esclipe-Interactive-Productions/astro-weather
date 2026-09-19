import customtkinter as ctk
from ui.settings import theme
from weatherapi import searchcity as getweather

button = ctk.CTkButton
label = ctk.CTkLabel
entry = ctk.CTkEntry

ctk.set_appearance_mode(theme)

weatherdata = None

def searchcity():
    cityname = searchentry.get()
    print(cityname)
    getweather(cityname)
    weatherdata = getweather(cityname)

app = ctk.CTk()
app.geometry("640x480")
app.title("astro weather")
app.resizable(False, False)

maintitle = label(app, text="astro weather", font=("Times", 15))
maintitle.place(x=10, y=5)
searchentry = entry(app, width=160, font=("Times", 11), placeholder_text="insert city name")
searchentry.place(x=100, y=5)
searchbutton = button(app, text="search", font=("Times", 11), width=55, fg_color="green", hover_color="dark green", command=searchcity)
searchbutton.place(x=275, y=5)
settingsbutton = button(app, text="settings", font=("Times", 11), fg_color="green", hover_color="dark green", width=70)
settingsbutton.place(x=550, y=5)

def weatherdescription():
    descriptionlabel = label(app, text="", font=("Times", 14))
    descriptionlabel.place(x=40, y=200)
    return weatherdata
app.mainloop()
