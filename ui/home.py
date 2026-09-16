import customtkinter as ctk
from ui.settings import theme
from weatherapi import searchcity as getweather


button = ctk.CTkButton
label = ctk.CTkLabel
entry = ctk.CTkEntry

ctk.set_appearance_mode(theme)

def searchcity():
    cityname = searchentry.get()
    print(cityname)
    getweather(cityname)

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

app.mainloop()
