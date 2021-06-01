from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import pyperclip

#Funcation File Location
Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please choose a folder",fg="red",font=("Arial",10))
    
def downloadVideo():
    choice = youtubeChoices.get()
    url = youtubeEntry.get()

    if(len(url) > 1):
        youtubeError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).get_highest_resolution()
            print ("highest resolution"+ url)
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True).get_lowest_resolution()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        elif(choice == choices[3]):
            select = yt.streams.filter(only_video=True).first()
        else:
            youtubeError.config(text="Link not valid!",fg="red")

    # Download Function
    select.download(Folder_Name)
    youtubeError.config(text="Download completed!")
#App Design
app = Tk()
winIcon = PhotoImage(file="app_icon.png")
app.config(bg="white")
app.iconphoto(False, winIcon)
app.resizable(False, False)
app.title("YouTube Downloader v0.1")
app.geometry("350x220")
app.columnconfigure(0,weight=1) #center content


#App Title
youtubelabel = Label(app,text="YouTube Downloader",font=("Arial",15),fg="black",bg="white",width=50)
youtubelabel.grid()

#Step1
youtubelabel = Label(app,text="Step 1: Paste Link", font=("Arial",10),width=50,bg="white")
youtubelabel.grid()

#String Text Field for Youtube URL
youtubeEntryVar = StringVar()
youtubeEntry = Entry(app,width=50, textvariable=youtubeEntryVar)
youtubeEntry.grid()

#Paste from Clipboard Button
#Room for Code

#Error Message Youtube URL
youtubeError = Label(app,text="Error Message", fg="red", font=("Arial",10))
#youtubeError.grid()

#Label for Save File
#saveLabel = Label(app,text="Save Video",font=("Arial",10,"bold"))
#saveLabel.grid()

#Step2 Choose Download Quality
youtubeQuality = Label(app,text="Step 2: Select Video Quality",font=("Arial",10),width=50,bg="white")
youtubeQuality.grid()

#Download Quality Dropdown
choices = ("Highest Resolution", "Lowest Resolution", "Audio Only", "Video Only")
youtubeChoices = ttk.Combobox(app,values=choices,state="readonly",width=30)
youtubeChoices.grid()

#Step3
youtubelabel = Label(app,text="Step 3: Choose Save Folder", font=("Arial",10),width=50,bg="white")
youtubelabel.grid()

#Button for Save File
saveEntry = Button(app,width=20,bg="white",text="Browse Folder",command=openLocation)
saveEntry.grid()

#Error Message for File Location
locationError = Label(app,text="",font=("Arial",10),bg="white",width=50)
locationError.grid()

#Download Youtube Video Button
downloadButton = Button(app,text="Get it!",width=40,bg="red",fg="white",command=downloadVideo)
downloadButton.grid()

#Footer
#devLabel = Label(app,text="jensbertram.de",font=("Arial",10))
#devLabel.grid()

app.mainloop()