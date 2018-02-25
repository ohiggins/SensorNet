#!/usr/bin/python env
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import time


root = Tk()
root.wm_title("SensorNet Demo")
#root.wm_attributes('-fullscreen','true')
root.config(width=720, height=480)
root.resizable(0,0)
#root.overrideredirect(True)

def clock():
    #update temp
    r = requests.get(url='http://10.0.0.239/json')
    tempValue2.config(text=str(r.json()[0]['temp']))
    humidValue2.config(text=str(r.json()[0]['humid']))
    r = requests.get(url='http://10.0.0.230/json')
    currentValue=r.json()[0]['analog']
    analogValue3.config(text=str(r.json()[0]['analog']))
    progress['value']=(r.json()[0]['analog']/255)*100
    ##Do something. This toggles the LED on the other Nodeumcu
    if currentValue>=128:
        if LEDValue2['text']=="OFF":
            swLED2()
    else:
        if LEDValue2['text']=="ON":
            swLED2()
    root.after(100,clock) 

def swLED1():
    r = requests.get(url='http://10.0.0.238/led')
    print(r.json()[0]['LED'])
    LEDValue1.config(text=str(r.json()[0]['LED']))
    return

def swLED2():
    r = requests.get(url='http://10.0.0.239/led')
    print(r.json()[0]['LED'])
    LEDValue2.config(text=str(r.json()[0]['LED']))
    return

def swLED3():
    r = requests.get(url='http://10.0.0.230/led')
    print(r.json()[0]['LED'])
    LEDValue3.config(text=str(r.json()[0]['LED']))
    return

nb = ttk.Notebook(root)
page1 = ttk.Frame(nb,width=800, height=470)

r = requests.get(url='http://10.0.0.238/name')
lblFrmSimple1=LabelFrame(page1,text=str(r.json()[0]['NAME']))
lblFrmSimple1.place(x=1,y=1,width=266,height=400)
ipLabel1 = Label(page1, text="IP:")
ipLabel1.place(x=5,y=20)
ipValue1 = Label(page1, text=str(r.json()[0]['IP']))
ipValue1.place(x=25,y=20)

r = requests.get(url='http://10.0.0.238/json')
LEDLabel1 = Label(page1, text="LED:")
LEDLabel1.place(x=5,y=40)
LEDValue1 = Label(page1, text=str(r.json()[0]['led']))
LEDValue1.place(x=35,y=40)
#temp
tempLabel1 = Label(page1, text="Temp:")
tempLabel1.place(x=5,y=60)
tempValue1 = Label(page1, text=str(r.json()[0]['temp']))
tempValue1.place(x=50,y=60)
#Humidity
humidLabel1 = Label(page1, text="Humid:")
humidLabel1.place(x=5,y=80)
humidValue1 = Label(page1, text=str(r.json()[0]['humid']))
humidValue1.place(x=50,y=80)


LEDButton1=Button(lblFrmSimple1,text="LED Switch",command=swLED1, width=13, height=3)
LEDButton1.place(x=5,y=125)

#2
r = requests.get(url='http://10.0.0.239/name')
lblFrmSimple2=LabelFrame(page1,text=str(r.json()[0]['NAME']))
lblFrmSimple2.place(x=267,y=1,width=266,height=400)
ipLabel2 = Label(page1, text="IP:")
ipLabel2.place(x=267+5,y=20)
ipValue2 = Label(page1, text=str(r.json()[0]['IP']))
ipValue2.place(x=267+25,y=20)

r = requests.get(url='http://10.0.0.239/json')
LEDLabel2 = Label(page1, text="LED:")
LEDLabel2.place(x=267+5,y=40)
LEDValue2 = Label(page1, text=str(r.json()[0]['led']))
LEDValue2.place(x=267+35,y=40)

LEDButton2=Button(lblFrmSimple2,text="LED Switch",command=swLED2, width=13, height=3)
LEDButton2.place(x=5,y=125)
#temp
tempLabel2 = Label(page1, text="Temp:")
tempLabel2.place(x=267+5,y=60)
tempValue2 = Label(page1, text=str(r.json()[0]['temp']))
tempValue2.place(x=267+50,y=60)
#Humidity
humidLabel2 = Label(page1, text="Humid:")
humidLabel2.place(x=267+5,y=80)
humidValue2 = Label(page1, text=str(r.json()[0]['humid']))
humidValue2.place(x=267+50,y=80)


##3
r = requests.get(url='http://10.0.0.230/name')
lblFrmSimple3=LabelFrame(page1,text=str(r.json()[0]['NAME']))
lblFrmSimple3.place(x=534,y=1,width=266,height=400)
ipLabel3 = Label(page1, text="IP:")
ipLabel3.place(x=534+5,y=20)
ipValue3 = Label(page1, text=str(r.json()[0]['IP']))
ipValue3.place(x=534+25,y=20)

r = requests.get(url='http://10.0.0.230/json')
LEDLabel3 = Label(page1, text="LED:")
LEDLabel3.place(x=534+5,y=40)
LEDValue3 = Label(page1, text=str(r.json()[0]['led']))
LEDValue3.place(x=534+35,y=40)

#analog
analogLabel3 = Label(page1, text="Analog:")
analogLabel3.place(x=534+5,y=60)
analogValue3 = Label(page1, text=str(r.json()[0]['analog']))
analogValue3.place(x=534+55,y=60)
progress = ttk.Progressbar(lblFrmSimple3, orient="horizontal", length=255, mode="determinate")
progress.place(x=5,y=80)
progress['value']=(r.json()[0]['analog']/255)*100
LEDButton3=Button(lblFrmSimple3,text="LED Switch",command=swLED3, width=13, height=3)
LEDButton3.place(x=5,y=125)

nb.add(page1, text='SensorNet Demo')
nb.pack(expand=1, fill="both")



clock()
root.wait_visibility()

root.mainloop()
