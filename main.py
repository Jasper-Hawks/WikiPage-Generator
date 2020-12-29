from tkinter import *
import os

# Author: Jasper Hawks 
# Created on December 27 2020   
# Create an HTML file creation front end
# for use in my Wiki Website 

def GenFile(): 

    # Generates a file written with submitted data, deletes the previous one, and repeats until 
    # we have one file with all of the data submitted  

    try: 
        with open("template.html") as oFile, open("1.html","w") as nFile:
            
            text = oFile.read()
            textTab = text.replace("<title>Tab Template</title>", "<title>" + EntryTitle.get() + "</title>", 1)
            nFile.write(textTab)
            
        with open ("1.html") as tFile, open ("2.html", "w") as bFile: 

            text = tFile.read()
            textTitle = text.replace("<h1>Jasper Hawks</h1>", "<h1>" + EntryTitle.get() + "</h1>", 1)
            bFile.write(textTitle)
            os.remove("1.html")
        
        with open ("2.html") as bFile, open ("3.html", "w") as hFile:
            
            text = bFile.read()
            textBio = text.replace("<p>Lorem</p>", "<p>"+ EntryBio.get("1.0", "end")+"</p>", 1)
            hFile.write(textBio)
            os.remove("2.html")
        
        with open ("3.html") as hFile, open (EntryTitle.get() + ".html", "w") as fFile:
            
            text = hFile.read()
            textHis = text.replace("<p>ipsum</p>", "<p>"+ EntryHis.get("1.0", "end")+"</p>", 1)
            fFile.write(textHis)
            os.remove("3.html")
        
        lblS = Label(root, text = "File created successfully", font="TKTextFont")
        lblS.place(x = 0, y = 500)

    except FileNotFoundError:

        lblError = Label(root, text = "Error template.html File Not Found: Make sure that the Generator and the \ntemplate.html file are in the same directory", font="TKTextFont")
        lblError.place(x = 0, y = 500)

root = Tk()
root.title("Page Generator")
root.resizable(False,False)

mainCanvas = Canvas(root,height=900,width=700)
mainCanvas.grid()

imgText = "Select File"

lblTitle = Label(root, text="Enter Title:",font="TKTextFont")
lblTitle.place(x = 5,  y = 0)

EntryTitle = Entry(root, bd = 5)
EntryTitle.place(x = 130, y = 0)

lblBio = Label(root, text="Enter Bio:",font="TKTextFont")
lblBio.place(x = 5, y =30)

EntryBio = Text(root, bd = 5)
EntryBio.place(x = 130, y = 30,width = 400,height = 200)

lblHis = Label(root, text="Enter History:",font="TKTextFont")
lblHis.place(x = 5, y =260)

EntryHis = Text(root, bd = 5)
EntryHis.place(x = 130, y = 260,width = 400,height = 200)

btnCreate = Button(root, text = "Create HTML file", command = GenFile)
btnCreate.place(x = 250, y = 800)

root.mainloop()