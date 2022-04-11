from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import pandas as pd
from openpyxl import load_workbook
import sqlite3

cxn = sqlite3.connect('grounds.db')

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
    for i in urls[2:3]:
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
    x = soup.find('div', attrs={"id": "dvGroundDetails"})
    headings = []

    for hea in x.find_all("h3"):
        headings.append(hea.text.replace('\n', ' ').strip())
    head_count = 0
    for table in x.find_all("table"):
        joke = []
        joke.append(headings[head_count])
        table_data_m.append(joke)
        head_count = head_count + 1
        for tr in table.find_all("tr")[:4]:
            newrow = []
            for td in tr.find_all("td"):
                newrow.append(td.text.replace('\n', ' ').strip())
            table_data_m.append(newrow)
        for tr2 in table.find_all("tr")[4:5]:
            new = []
            bs = []
            for u in tr2.find_all("u"):
                bs.append(u.text.replace('\n', ' ').strip())
                new.append(bs)
            bs_count = 0
            new = new[0]

            toll = []
            toll.append(new[0])

            table_data_m.append(toll)
            bs_count = bs_count + 1

            for ul in tr2.find_all("ul"):
                tp = new[bs_count]
                to_add=[]
                to_add.append(tp)
                table_data_m.append(to_add)
                bs_count = bs_count + 1
                for li in ul.find_all("li"):
                    ls = []
                    ls.append(li.text.replace('\n', ' ').strip())
                    table_data_m.append(ls)
        rows = []

        # print(table_data_m)
        for i in table_data_m[0:1]:
            for check in i:
                hmm = check[0:]
                rows.append(hmm)

        for i in table_data_m[1:5]:
            for check in i:
                index = check.find(':')
                add_tosql = check[index+1:]
                rows.append(add_tosql)
        str = " "
        res = [''.join(ele) for ele in table_data_m[6:]]
        for ele in res:
            str = str + " " + ele
        
        rows.append(str)
        print(rows)
        
        conn = sqlite3.connect('grounds.db')
        c = conn.cursor()
        query = 'INSERT INTO Grounds VALUES("' + rows[0] + '","' + rows[1] + '","' + rows[2] + '","' + rows[3] + '","' + rows[4] + '","' + rows[5] +'")'
        #query = 'INSERT INTO Grounds VALUES(' + myname + ')'
        print(query)
        execute = c.execute(query)
        conn.commit()   
        
        
cxn.commit()