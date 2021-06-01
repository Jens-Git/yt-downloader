from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#Funcation File Location
Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please choose a folder",fg="red")
    
def downloadVideo():
    choice = youtubeChoices.get()
    url = youtubeEntry.get()

    if(len(url) > 1):
        youtubeError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).get_highest_resolution()
        elif(choice == choice[1]):
            select = yt.streams.filter(progressive=True).get_lowest_resolution()
        elif(choice == choice[2]):
            select = yt.streams.filter(progressive=True).get_audio_only()
        else:
            youtubeError.config(text="Link not valid!",fg="red")

    # Download Function
    select.download(Folder_Name)
    youtubeError.config(text="Download completed!")



#App Design
app = Tk()
app.title("Youtube Downloader")
app.mainloop()
app.geometry("350x400")
app.columnconfigure(0,weight=1) #center content

#App Title
youtubelabel = Label(app,text="Youtube Downloader", font=("Arial",15))
youtubelabel.grid()

#String Text Field for Youtube URL
youtubeEntryVar = StringVar()
youtubeEntry = Entry(app,width=50, textvariable=youtubeEntryVar)
youtubeEntry.grid()

#Error Message Youtube URL
youtubeError = Label(app,text="Error Message", fg="red", font=("jost",10))
youtubeError.grid()

#Label for Save File
saveLabel = Label(app,text="Save Video",font=("jost",15,"bold"))
saveLabel.grid()

#Button for Save File
saveEntry = Button(app,width=10,bg="red",fg="white",text="Choose File",command=openLocation)
saveEntry.grid()

#Error Message for File Location
locationError = Label(app,text="Error Msg of Path",font=("jost",15))
locationError.grid()

#Choose Download Quality
youtubeQuality = Label(app,text="Select Quality",font=("jost",15))
youtubeQuality.grid()

#Download Quality Dropdown
choices = ("Highest", "Lowest", "Audio Only")
youtubeChoices = ttk.Combobox(app,values=choices)
youtubeChoices.grid()

#Download Youtube Video Button
downloadButton = Button(app,text="Download",width=10,bg="red",fg="white",command=downloadVideo)
downloadButton.grid()

#Footer
devLabel = Label(app,text="jensbertram.de",font=("jost",15))
devLabel.grid()

app.mainloop()
