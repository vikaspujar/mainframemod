import urllib.request
import urllib.parse
import string
import json
import tkinter
import requests
from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import ttk



#Code for screen1
def screen1():

    root.destroy()
    global root1
    root1 = Tk()
    root1.geometry('550x400')
    head = Label(root1, text="ABC BANK LTD\n",font=("Arial Bold", 10,))
    head.grid(column=5, row=2)
    head = Label(root1, text="CUSTOMER INFORMATION",font=("Arial Bold", 10))
    head.grid(column=5, row=5)
    #res = "Welcome to " + txt1.get()
    #head.configure(text= res)
    variable1=StringVar()
    ttk.Label(root1, text="Customer Code").grid(column=4, row=6, sticky=W)
    ttk.Entry(root1, width=20, textvariable=variable1).grid(column=5, row=6)
    ttk.Label(root1, text="Customer Name").grid(column=4, row=10, sticky=W)
    indata2 = Entry(root1)
    indata2.grid(row=10, column=5)
    ttk.Label(root1, text="Customer Dob").grid(column=4, row=14, sticky=W)
    indata3 = Entry(root1)
    indata3.grid(row=14, column=5)
    ttk.Label(root1, text="Customer Bal").grid(column=4, row=18, sticky=W)
    indata4 = Entry(root1)
    indata4.grid(row=18, column=5)
    ttk.Label(root1, text="Customer Tel No").grid(column=4, row=20, sticky=W)
    indata4 = Entry(root1)
    indata4.grid(row=20, column=5)
    ttk.Button(root1, text="Get All details", command = screen2).grid(column=4, row=26, sticky=W)
    ttk.Button(root1, text="Get Catg Code", command = screen2).grid(column=5, row=26, sticky=W)

    root1.mainloop()
    return


#Code to get data from JSON end point
url = requests.get('http://cap-sg-prd-2.integration.ibmcloud.com:16908/custCatg/cust/21018')
data = json.loads(url.text)
print(data)
#for nested json need to access them with mutiple []
acct_number = data["CUSTREADOperationResponse"]['ws_cust_rec'] ['cust_code']
catg_code =  data["CUSTREADOperationResponse"]['ws_cust_rec'] ['cust_catg']

#Code for screen2
def screen2():
    root1.destroy()
    root2 = Tk()
    root2.geometry('550x400')
    root2.title("ABC Bank Limited")

    mainframe = ttk.Frame(root2, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)


    #Populate Values
    ttk.Label(mainframe, text=acct_number, font=("Arial Bold", 10)).grid(column=2, row=2, sticky=W)
    ttk.Label(mainframe, text=catg_code, font=("Arial Bold", 10)).grid(column=2, row=4, sticky=W)


    #Heading Details
    ttk.Label(mainframe, text="ABC Bank",font=("Arial Bold", 18)).grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="Customer Code : ", font=("Arial Bold", 10)).grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="Customer Catg : ", font=("Arial Bold", 10)).grid(column=1, row=4, sticky=W)

    root2.mainloop()
    return

#Main screen code
root = Tk()
root.geometry('350x200')
root.title("Welcome")
lbl = Label(root, text = 'Username')
lbl.grid(column=1,row=1)
txt1 = Entry(root, width=20)
txt1.grid(column=2, row=1)
lb2 = Label(root, text = 'Password')
lb2.grid(column=1,row=2)
txt2 = Entry(root, width=20)
txt2.grid(column=2, row=2)

ttk.Button(root, text="Login", command = screen1).grid(column=2, row=4, sticky=W)
root.mainloop()



