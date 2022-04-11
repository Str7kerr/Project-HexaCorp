from os import name
import sqlite3
import pandas as pd
from tkinter import *
from tkinter import filedialog
from xlsxwriter.workbook import Workbook
#from read_umpire import *

cxn = sqlite3.connect('umpires.db')

from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import pandas as pd
from openpyxl import load_workbook
url = "http://millenniumcricketleague.com/Home/Results.aspx?tt=1"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
x = soup.find_all('table', attrs={"class": "GridViewStyle"})[2]
stock = []
table_data = []

for tr in x.tbody.find_all("tr"):
    t_row = []
    newrow = []
    url = []
    urls = []
    i=0
    for td in tr.find_all("td"):
        newrow.append(td.text.replace('\n', ' ').strip())
        
        for a in td.find_all('a',{"href":True}):
            urls.append(a['href'])
    for i in urls[3:4]:
        str1 = "http://millenniumcricketleague.com/Home/"
        i = str1 + i
        stock.append(i)
        newrow.append(i)
    table_data.append(newrow)



for i in stock:
    print(i)
    table_data_m = []
    
    # for th in x.find_all("th"):
    #     t_headers.append(th.text.replace('\n', ' ').strip())
    #     table_data_m.append(t_headers)
    html_content = requests.get(i).text
    soup = BeautifulSoup(html_content, "lxml")
    x = soup.find('div', attrs={"id":"dvUmpireDetails"})
    headings = []
    
    for hea in x.find_all("h3"):
        headings.append(hea.text.replace('\n', ' ').strip())
    head_count = 0
    for table in x.find_all("table")[1:]:
        joke =[]
        joke.append(headings[head_count])
        table_data_m.append(joke)
        head_count = head_count+1
        # table_data_m.append(headings[head_count].replace('\n', ' ').strip())
        # head_count = head_count+1
        if(table.find("th")):
            t_headers = []
            for th in table.find_all("th"):
                t_headers.append(th.text.replace('\n', ' ').strip())
                # print(t_headers)
            table_data_m.append(t_headers)
            


        for tr in table.find_all("tr"):
            newrow = []
            for td in tr.find_all("td"):
                newrow.append(td.text.replace('\n', ' ').strip())
            table_data_m.append(newrow)
        joke2=[]
        joke2.append(headings[head_count])
        table_data_m.append(joke2)    
        break
    y = soup.find('table',attrs={"class": "GridViewStyle"})
    
    t_headers = []
    for th in y.find_all("th"):
        t_headers.append(th.text.replace('\n', ' ').strip())
        # print(t_headers)
    table_data_m.append(t_headers)
    for tr in y.find_all("tr"):
        newrow = []
        for td in tr.find_all("td"):
            newrow.append(td.text.replace('\n', ' ').strip())
        table_data_m.append(newrow)
    rows = []
    # print(table_data_m)
    history = []
    
    
    for i in table_data_m[1:6]:
        for check in i:
            index = check.find(':')
            add_tosql = check[index+1:]
            rows.append(add_tosql)
    for i in table_data_m[7:]:
        rows.append(i)
    rows2add = [k for k in rows if k!=[]]
    print(rows2add[5])
    
    conn = sqlite3.connect('umpires.db')
    c = conn.cursor()
    query = 'INSERT INTO Umpires VALUES("' + rows[0] + '","' + rows[1] + '","' + rows[2] + '","' + rows[3] + '","' + rows[4] + '")'
    #query = 'INSERT INTO Umpires VALUES(' + myname + ')'
    print(query)
    # execute = c.execute(query)
    # conn.commit()
    # break
    

                



    table_data_m2 = [k for k in table_data_m if k!=[]]





    
        


# print(table_data_m2)


        


cxn.commit()