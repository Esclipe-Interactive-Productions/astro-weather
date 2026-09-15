import customtkinter
from ui.settings import theme

customtkinter.set_appearance_mode(theme)

app = customtkinter.CTk()
app.geometry("640x480")
app.title("astro weather")
app.resizable(False, False)


app.mainloop()
