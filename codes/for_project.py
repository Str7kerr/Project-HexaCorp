from check import query
from tkinter import *
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import sqlite3


root1 = Tk()
cxn = sqlite3.connect('newdatabase.db')
cursor = cxn.cursor()

def update():
    for i in rows:
        trv.insert('','end',values=i)

wrapper1 = LabelFrame(root1,text="Files")
wrapper2 = LabelFrame(root1, text="New")
wrapper3 = LabelFrame(root1, text = "Data")

wrapper1.pack(fill="both", expand="yes",padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes",padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes",padx=20, pady=10)

trv = ttk.Treeview(wrapper1,columns = (1,2,3,4), show= "headings", height="6")
trv.heading(1, text="Customer ID")
trv.heading(2,text="First Name")
trv.heading(3, text="Last Name")
trv.heading(4, text="Age")


query = "SELECT * FROM mytable"
cursor.execute(query)
rows = cursor.fetchall()
update(rows) 
root1.title("My App")
root1.geometry("500x400")
root1.mainloop()

