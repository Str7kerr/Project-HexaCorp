import enum
import sqlite3
import pandas as pd
from tkinter import *
from tkinter import filedialog
from xlsxwriter.workbook import Workbook


root = Tk()
cxn = sqlite3.connect('newdatabase.db')

# e = Entry(root)
# e.pack()

myText1 = Label(root, text="Would you like to add a single or multiple files?")
myText1.grid(row=0, column=2, columnspan=2, padx=42)


def openFile():
    filepath = filedialog.askopenfilename(title='Choose a file')
    df = pd.read_excel(filepath, sheet_name=None)
    
    for sheet in df:
        df[sheet].to_sql(name='mytable', con=cxn, if_exists='append')


def openFiles():
    filepath = filedialog.askopenfilenames(title='Choose files')
    for itr in filepath:
        df = pd.read_excel(itr, sheet_name=None)
        

        for sheet in df:
            df[sheet].to_sql(name='mytable', con=cxn, if_exists='append')


myButton1 = Button(root, text="Single File",bg = '#0096FF', fg = 'white', command=openFile)
myButton1.grid(row=1, column=2, pady=5)
myButton2 = Button(root, text="Multiple Files",bg = '#0096FF', fg = 'white', command=openFiles)
myButton2.grid(row=1, column=3)


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
#    for i in range(len(names)):
#        col_name = Entry(root,relief='solid',width=20, font=('HP Simplified', 12))
#        col_name.grid(row=6, column=i,sticky=NSEW)
#        col_name.insert(END,names[i])
    col_name1 = Entry(root,relief='solid',width=10, font=('HP Simplified', 12))
    col_name1.grid(row=6, column=0,sticky=NSEW)
    col_name1.insert(END,names[0])
    col_name2 = Entry(root,relief='solid',width=40, font=('HP Simplified', 12))
    col_name2.grid(row=6, column=1,sticky=NSEW)
    col_name2.insert(END,names[1])
    col_name3 = Entry(root,relief='solid',width=50, font=('HP Simplified', 12))
    col_name3.grid(row=6, column=2,sticky=NSEW)
    col_name3.insert(END,names[2])
    r_set = c.execute(query)
    i = 0
    for r in r_set:
        for j in range(len(r)):
            e = Entry(relief='solid',width=20, font=('Arial', 10, 'bold'))
            e.grid(row=i+8, column=j,sticky=NSEW) 
            e.insert(END, r[j])
        i=i+1
    # dataLabel = Label(root, text=e)


#   answeer = pd.read_sql(query, conn)
#    query_label = Label(root, text = answeer)
#    query_label.grid(row=5,column=2)
show_button = Button(root, text="Show Records",  bg = '#0096FF', fg = 'white',command=query)
show_button.grid(row=2, column=2, pady=5)


def delete():
    conn = sqlite3.connect('newdatabase.db')
    c = conn.cursor()
    delete_query = 'DELETE FROM mytable;'
    
    c.execute(delete_query)
    conn.commit()
    
#def alter():
#    conn = sqlite3.connect('newdatabase.db')
#    c = conn.cursor()
#    alter_query = 'ALTER TABLE mytable ADD Wins INT; '
#    c.execute(alter_query)
#    conn.commit()
#new_column_button = Button(root, text='Add Column', command=alter).grid(row = 2,column=3)

def fill():
    fill_query = 'UPDATE mytable SET filename = "SAMPLE" WHERE filename IS NULL;'
    conn = sqlite3.connect('newdatabase.db')
    c = conn.cursor()
    exectoo = c.execute(fill_query)
    conn.commit()




def getData():
    topo = 'ALTER table mytable ADD COLUMN filename VARCHAR(30);'
    conn = sqlite3.connect('newdatabase.db')
    c = conn.cursor()
    exec = c.execute(topo)
    conn.commit()
    fill()
#    new_data = pd.DataFrame(data_new)
#    file_name = 'new.xlsx'
#    new_data.to_excel(file_name)

add_column = Button(root,text='Add Column',bg = '#0096FF', fg = 'white', command=getData).grid(row = 3,column=2)



delete_button = Button(root, text='Delete Records',bg = '#0096FF', fg = 'white', command=delete)
delete_button.grid(row=2, column=3)

def finale():
    workbook = Workbook('final.xlsx')
    worksheet = workbook.add_worksheet()
    conn=sqlite3.connect('newdatabase.db')
    c=conn.cursor()
    mysel=c.execute("select * from mytable")
    this_one = c.execute("select * from mytable")
    names = list(map(lambda x: x[0],
                    this_one.description))
    for i in range(len(names)):
        worksheet.write(0,i,names[i])   
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1,j, value)
    workbook.close()
    conn.commit()

to_button = Button(root, text='To Excel',bg = '#0096FF', fg = 'white', command=finale)
to_button.grid(row=3, column=3)

cxn.commit()    
root.mainloop()