import sqlite3
import pandas as pd
from tkinter import *
from tkinter import filedialog
import numpy as np

root = Tk()
cxn = sqlite3.connect('newdatabase.db')

# e = Entry(root)
# e.pack()

myText1 = Label(root, text="Would you like to add a single or multiple files?")
myText1.grid(row=0, column=2, padx=42)


def openFile():
    filepath = filedialog.askopenfilename(title='Choose a file')
    df = pd.read_excel(filepath, sheet_name=None)
    for sheet in df:
        df[sheet].to_sql(name='mytable', con=cxn, if_exists='append')


def openFiles():
    filepath = filedialog.askopenfilenames(title='Choose files')
    for itr in filepath:
        df = pd.read_excel(itr, sheet_name=None)
        #    df = pd.read_excel(filepath, sheet_name = None)
        for sheet in df:
            df[sheet].to_sql(name='mytable', con=cxn, if_exists='append')


myButton1 = Button(root, text="Single File",bg = '#0096FF', fg = 'white', command=openFile)
myButton1.grid(row=1, column=2, pady=5)
myButton2 = Button(root, text="Multiple Files", command=openFiles)
myButton2.grid(row=2, column=2)


def query():
    conn = sqlite3.connect('newdatabase.db')
    c = conn.cursor()
    # c.execute("SELECT *, oid FROM mytable")
    # records = c.fetchall()
    # print(records)
    # print_records = ''
    # for record in records:
    #     print_records +=  str(record[1]) + "  " + str(record[2])+  "  " + str(record[3]) + "\n"

    query = 'SELECT  * FROM mytable ;'
    this_one = c.execute(query)
    names = list(map(lambda x: x[0],
                    this_one.description))
    for i in range(len(names)):
        col_name = Entry(root,relief='solid', width = 10,font=('HP Simplified', 12))
        col_name.grid(row=6, column=i,sticky=NSEW)
        col_name.insert(END,names[i])
    r_set = c.execute(query)
    i = 0
    for r in r_set:
        for j in range(len(r)):
            e = Entry(relief='solid',width=22, font=('Arial', 10, 'bold'))
            e.grid(row=i+8, column=j,sticky=NSEW) 
            e.insert(END, r[j])
        i=i+1
    # dataLabel = Label(root, text=e)



show_button = Button(root, text="Show Records", command=query)
show_button.grid(row=3, column=2, pady=5)


def delete():
    conn = sqlite3.connect('newdatabase.db')
    c = conn.cursor()
    delete_query = 'DELETE FROM mytable;'
    c.execute(delete_query)
    conn.commit()
    
def alter():
    conn = sqlite3.connect('newdatabase.db')
    c = conn.cursor()
    alter_query = 'ALTER TABLE mytable ADD Wins INT; '
    c.execute(alter_query)
    conn.commit()
new_column_button = Button(root, text='Add Column', command=alter).grid(row = 2,column=3)



delete_button = Button(root, text='Delete Records', command=delete)
delete_button.grid(row=4, column=2)
cxn.commit()    
root.mainloop()