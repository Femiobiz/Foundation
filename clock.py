from time import strftime
from tkinter import *
import tkinter

def clock():
    time = strftime('%I:%M:%S %p')
    lblClock.config(text=time, relief='raised')
    lblClock.after(1000,clock)
    lblClock.pack(pady=20)

root = Tk()
root.geometry('400x100')
root.title('My Digital Clock')
root.resizable(False, False)
# Label into root
lblClock = Label(root, fg='black', font=('arial', 26, 'bold'))
clock()
root.mainloop()


# #### Json #####
# import json
# # To exchnge information through the server it has to be converted to Json using '.dumps' and object can be retrieved from 
# # Json using '.load' object has to be in form of dictionary
# obj = {'name': 'Adebayo', 'age': 35, 'marital': 'single'}
# js = json.dumps(obj,indent=4)
# print(js)