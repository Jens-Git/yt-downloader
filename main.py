from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

app = Tk()
app.title("Youtube Downloader")
app.mainloop()
app.geometry("350x400")
app.columnconfigure(0,weight=1) #center content

youtubelabel = Label(app,text="Youtube Downloader", font=("Arial",15))
youtubelabel.grid()
