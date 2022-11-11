import requests
import tkinter
from tkinter import *

# Acess api
link = 'https://api.adviceslip.com/advice'
request = requests.get(link)
request_json = request.json()
advice = request_json.get('slip').get('advice')
#print(advice)

# Window

master = Tk()
master.title('Minuts of wisdom')
master.geometry('490x560+650+200')
title = Label(master, text='Minuts of wisdom', font=('Verdana', 17, 'bold'))
title.place(width=305, height=30, x=90  , y=10)


master.mainloop()