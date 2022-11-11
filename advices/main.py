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
master.minsize(490, 560)
master.maxsize(490, 560)
background = PhotoImage(file='images/master.png')
background_master = Label(master, image=background)
background_master.pack()


# Content

cont = len(advice)

title = Label(master, text='Minuts of wisdom', font=('Verdana', 24, 'bold'), fg='#FFFFFF', background='black')
title.place(width=315, height=30, x=90, y=10)

def click_advice():

    result = Label(master, text=advice[0:46], font=('Verdana', 12, 'bold'), justify=CENTER, fg='#FFFFFF', background='black')
    result.place(width=472, height=40, x=10, y=220)
    result_comp = Label(master, text=advice[47:96], font=('Verdana', 12, 'bold'), justify=CENTER, fg='#FFFFFF', background='black')
    result_comp.place(width=472, height=40, x=10, y=250)

    button_close = Button(master, text='Close', font=('Verdana', 12, 'bold'), command=master.destroy)
    button_close.place(width=100, height=30, x=204, y=300)



button = Button(master, text='Click here to your advice!', font=('Verdana', 12, 'bold'), command=click_advice)
button.place(width=305, height=30, x=94, y=180)


master.mainloop()