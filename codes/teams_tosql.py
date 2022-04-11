from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import pandas as pd
from openpyxl import load_workbook
import sqlite3

cxn = sqlite3.connect('teams.db')

url = "http://millenniumcricketleague.com/Home/Results.aspx?tt=1"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
x = soup.find_all('table', attrs={"class": "GridViewStyle"})[2]

stock = []

data = {}
table_data = []

for tr in x.tbody.find_all("tr"):
    t_row = []
    newrow = []
    url = []
    urls = []
    i = 0
    for td in tr.find_all("td"):
        newrow.append(td.text.replace('\n', ' ').strip())

        for a in td.find_all('a', {"href": True}):
            urls.append(a['href'])
    for i in urls[:2]:
        str1 = "http://millenniumcricketleague.com/Home/"
        i = str1 + i
        stock.append(i)
        newrow.append(i)
    table_data.append(newrow)


path = "F:\codes\grounds.xlsx"
writer = pd.ExcelWriter(path, engine='openpyxl')
counter = 1

for i in stock:
    print(i)
    
    table_data_m = []
    html_content = requests.get(i).text
    soup = BeautifulSoup(html_content, "lxml")
    x = soup.find('div', attrs={"id": "dvTeamDetails"})
    headings = []

    # for hea in x.find_all("h3"):
    #     headings.append(hea.text.replace('\n', ' ').strip())
    head_count = 0
    for table in x.find_all("table"):
        joke = []
        # joke.append(headings[head_count])
        # table_data_m.append(joke)
        # head_count = head_count + 1
        # print(table)
        
    
        for tr in table.find_all("tr"):
            newrow = []
            for td in tr.find_all("td"):
                newrow.append(td.text.replace('\n', ' ').strip())
            table_data_m.append(newrow)
        # rows = []

        # # print(table_data_m)
        # for i in table_data_m:
        #     rows.append(i)
        # print(rows)
        # for i in table_data_m[1:5]:
        #     for check in i:
        #         index = check.find(':')
        #         add_tosql = check[index+1:]
        #         rows.append(add_tosql)
        # str = " "
        # res = [''.join(ele) for ele in table_data_m[6:]]
        # for ele in res:
        #     str = str + " " + ele
        
        # rows.append(str)
        # print(rows)
    y = soup.find('table',attrs={"class": "GridViewStyle"})
    for tr in y.find_all("tr"):
        newrow = []
        for td in tr.find_all("td"):
            newrow.append(td.text.replace('\n', ' ').strip())
        table_data_m.append(newrow)
    rows = []
    
    for i in table_data_m[4:]:
        rows.append(i)
    flat_list = [item for sublist in rows for item in sublist]
    # print(flat_list)
    # for i in rows[2:4]:
    #     print(i)
    #-------------------------------------------------
    first_data = []
    for i in table_data_m[:3]:
        first_data.append(i)
    flat_out = [item for sublist in first_data for item in sublist]
    stroll = ""
    for i in flat_out:
        stroll+= i
        stroll+=","
    new_stroll = stroll[:-1]
    if(new_stroll[0] == ","):
        new_stroll = new_stroll[1:]
    #-------------------------------------------------
    first_col = []
    for i in rows[:3]:
        first_col.append(i)
    # print(first_col)
    flat_list2 = [item for sublist in first_col for item in sublist]
    flat_list3 = [k for k in flat_list2 if k!='']
    #-------------------------------------------------
    for i in rows[3:7]:
        print(i)
    
    # conn = sqlite3.connect('teams.db')
    # c = conn.cursor()
    # conn.execute('INSERT INTO Teams VALUES("' + new_stroll + '",(?),"' + flat_list[1] + '","' +flat_list[2] + '","' + flat_list[3] + '","' + flat_list[4] + '","' + flat_list[5] +'","' +flat_list[6] +'")',[','.join(flat_list3)])
    # #query = 'INSERT INTO Teams VALUES(' + myname + ')'
    # # print(query)
    # # execute = c.execute(query)
    # conn.commit()   
        
        
cxn.commit()