
from tkinter import * #tkinter gui lib, used for GUI
from tkinter import ttk, filedialog, messagebox #tkinter gui lib, used for GUI
from PIL import Image, ImageTk #pillow lib, used for image display in app
from pytube import YouTube #youtube lib, used for parsing youtube content

#Make script EXE-cutable
#Note: Images and Data must be called via resource_path(image.png)
import sys, os 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#Funcation File Location
Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        savebtntext.set(Folder_Name)
    #else:
        #messagebox.showinfo("YouTube Downloader", "Please choose a path to save your video!")
        #locationError.config(text="Please choose a folder",fg="red",font=("Raleway",10))
    
def downloadVideo():
    if (Folder_Name == ""):
        messagebox.showerror("YouTube Downloader", "Please choose a save folder")
    elif (youtubeChoices.get() == ""):
        messagebox.showerror("YouTube Downloader", "Please choose video quality")
    elif (youtubeEntry.get() == ""):
        messagebox.showerror("YouTube Downloader", "Please insert a YouTube link")
    
    choice = youtubeChoices.get()
    url = youtubeEntry.get()

    if(len(url) > 1):
        youtubeError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).get_highest_resolution()
            print ("Parsing Highest Resolution from "+ url +"...")
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True).get_lowest_resolution()
            print ("Parsing Lowest Resolution from "+ url + "...")
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
            print ("Parsing Audio Only from "+ url + "...")
        elif(choice == choices[3]):
            select = yt.streams.filter(only_video=True).first()
            print ("Parsing Video Only from "+ url + "...")
        else:
            youtubeError.config(text="Link not valid!",fg="red")

    
    # Download Function
    select.download(Folder_Name)
    #youtubeError.config(text="Download completed!")
    downloadbtntext.set ("Got it! One more time?")
    messagebox.showinfo("YouTube Downloader", "Download complete!")
#App Design
app = Tk()
winIcon = PhotoImage(file=resource_path("app_icon.png"))
app.config(bg="white")
app.iconphoto(False, winIcon)
app.resizable(False, False)
app.title("YouTube Downloader v0.2")

canvas = Canvas(app, height=320, bg="white", borderwidth=0, highlightthickness=0)
canvas.grid(columnspan=3, rowspan=8)

app_logo = Image.open(resource_path("app_icon_main.png")).resize((350,100), Image.ANTIALIAS)
app_logo = ImageTk.PhotoImage(app_logo)
app_logo_label = Label(image=app_logo,bg="white", relief="flat")
app_logo_label.image = app_logo 
app_logo_label.grid(columnspan=3, column=0, row=0)
#app.columnconfigure(0,weight=1) #center content


#App Title
#youtubelabel = Label(app,text="YouTube Downloader",font=("Raleway",15),fg="black",bg="white",width=50)
#youtubelabel.grid()

#Step1
youtubelabel = Label(app,text="Step 1: Paste Link", font=("Raleway",10),bg="white")
youtubelabel.grid(columnspan=2, column=0, row=1)

#String Text Field for Youtube URL
youtubeEntryVar = StringVar()
youtubeEntry = Entry(app,width=47, textvariable=youtubeEntryVar, relief="solid", bg="white")
youtubeEntry.grid(column=0, row=2)

#Paste from Clipboard Button
#Room for Code

#Error Message Youtube URL
youtubeError = Label(app,text="Error Message", fg="red", font=("Raleway",10))
#youtubeError.grid()

#Label for Save File
#saveLabel = Label(app,text="Save Video",font=("Raleway",10,"bold"))
#saveLabel.grid()

#Step2 Choose Download Quality
youtubeQuality = Label(app,text="Step 2: Select Video Quality",font=("Raleway",10),bg="white")
youtubeQuality.grid(column=0, row=3)

#Download Quality Dropdown
choices = ("Highest Resolution", "Lowest Resolution", "Audio Only", "Video Only")
youtubeChoices = ttk.Combobox(app,values=choices,state="readonly",width=44)
youtubeChoices.grid(column=0, row=4)

#Step3
youtubelabel = Label(app,text="Step 3: Choose Save Folder", font=("Raleway",10),width=50,bg="white")
youtubelabel.grid(column=0, row=5)

#Button for Save File
savebtntext = StringVar()
savebtntext.set("Browse Folder")
saveEntry = Button(app,width=40,bg="white",textvariable=savebtntext,command=openLocation,relief="solid",borderwidth=1)
saveEntry.grid(column=0, row=6)

#Error Message for File Location
#locationError = Label(app,text="",font=("Raleway",10),bg="white")
#locationError.grid(column=0, row=7)

#Download Youtube Video Button
downloadbtntext = StringVar()
downloadbtntext.set ("Get it!")
downloadButton = Button(app,textvariable=downloadbtntext,width=60, height=2, bg="red",fg="white",command=downloadVideo,relief="solid",borderwidth=1)
downloadButton.grid(columnspan=3, column=0, row=8)

#Footer
#devLabel = Label(app,text="jensbertram.de",font=("Raleway",10))
#devLabel.grid()

app.mainloop()