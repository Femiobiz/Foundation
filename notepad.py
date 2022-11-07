from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re
from datetime import datetime
import os
# End of module statement

# initializa root element from tk
root = Tk()

#Configuring root width and height
width = 800
height = 450
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw//2 - width//2
y = sh//2 - height//2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(False, False)


#setting icon to the root window
icon = PhotoImage(file ='icons/padicon.png')
root.iconphoto(False,icon)
root.title('New Notepad')




#Compilr and view notepad using mainloop 
root.mainloop()