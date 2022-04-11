import sqlite3
import pandas as pd
from tkinter import *
from tkinter import filedialog
import tkinter as tk

root = Tk()
cxn = sqlite3.connect('mydatabase.db')

#e = Entry(root)
#e.pack()

myText1 = Label(root,text="Would you like to add a single or multiple files?")
myText1.grid(row=0,column=3,padx=20)

def openFile():
    filepath = filedialog.askopenfilename(title= 'Choose a file')
    df = pd.read_excel(filepath,sheet_name=None)
    for sheet in df:
        df[sheet].to_sql(name = 'mytable',con=cxn,if_exists='append')
def openFiles():
    filepath = filedialog.askopenfilenames(title='Choose files')
    for itr in filepath:
        df = pd.read_excel(itr, sheet_name = None)
#    df = pd.read_excel(filepath, sheet_name = None)
        for sheet in df:
            df[sheet].to_sql(name = 'mytable',con=cxn,if_exists='append')

myButton1 =  Button(root, text = "Single File", command=openFile)
myButton1.grid(row=1,column=2,pady=5,padx=20)
myButton2 =  Button(root, text = "Multiple Files", command=openFiles)
myButton2.grid(row=1,column=4)

def query():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor() 
    # c.execute("SELECT *, oid FROM mytable")
    # records = c.fetchall()
    # print(records)
    # print_records = ''
    # for record in records:
    #     print_records +=  str(record[1]) + "  " + str(record[2])+  "  " + str(record[3]) + "\n"
    
    query = 'SELECT * FROM mytable'
    r_set=c.execute(query)
    names = list(map(lambda x: x[0],
                    r_set.description))
    for i in range(len):
        hehekiki = Label(root, text=names[i])
        hehekiki.grid(row =0,column=i)
#    i=0
#    for r in r_set: 
#        for j in range(len(r)):
#            e = Entry(relief=GROOVE)
#            e.grid(row=i+8, column=j,sticky=NSEW) 
#            e.insert(END, r[j])
#        i=i+1
    
    # dataLabel = Label(root, text=e)
#   answeer = pd.read_sql(query, conn)
#    query_label = Label(root, text = answeer)
#    query_label.grid(row=5,column=2)
show_button = Button(root,text="Show Records",command=query)
show_button.grid(row=3,column=3,pady=5)

def delete():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor() 
    print("Reached delete!")
    c.execute('DELETE FROM mytable WHERE Age = 40;')
    print("Passed the query")

delete_button = Button(root,text='Delete Records',command= delete).grid(row=4,column=3)
cxn.commit()
root.mainloop()
