import customtkinter as ctk
from ui.settings import theme
from weatherapi import data

button = ctk.CTkButton
label = ctk.CTkLabel
entry = ctk.CTkEntry

ctk.set_appearance_mode(theme)

app = ctk.CTk()
app.geometry("640x480")
app.title("astro weather")
app.resizable(False, False)

maintitle = label(app, text="astro weather", font=("Times", 15))
maintitle.place(x=10, y=5)
searchentry = entry(app, width=160, font=("Times", 11))
searchentry.place(x=100, y=5)

app.mainloop()
