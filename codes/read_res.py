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

data = {}
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
    for i in urls[4:5]:
        str1 = "http://millenniumcricketleague.com/Home/"
        i = str1 + i
        stock.append(i)
        newrow.append(i)
    table_data.append(newrow)
        # table_data_m = []
        # html_content = requests.get(i).text
        # soup = BeautifulSoup(html_content, "lxml")
        # x = soup.find_all('table')
        # for table in x[1:]:
        #     for tr2 in table.find_all("tr"):
        #         newrow2 = []
        #         for td2 in tr2.find_all("td"):
        #             newrow2.append(td2.text.replace('\n', ' ').strip())
        #         table_data_m.append(newrow2)
        #         print("Hi")

path = "F:\codes\Results2.xlsx"
writer = pd.ExcelWriter(path,engine='openpyxl')
counter = 1

for i in stock:
    print(i)
    table_data_m = []
    
    # for th in x.find_all("th"):
    #     t_headers.append(th.text.replace('\n', ' ').strip())
    #     table_data_m.append(t_headers)
    html_content = requests.get(i).text
    soup = BeautifulSoup(html_content, "lxml")
    x = soup.find('div', attrs={"id":"dvMatchScore"})
    # print(x)
    headings = []
    y = soup.find("h3")
    temp = []
    temp.append(y.text.replace('\n', ' ').strip())
    table_data_m.append(temp)
    for table1 in x.find_all("table")[:1]:
        for tr1 in table1.find_all("tr")[:2]:
            
            for td1 in tr1.find_all("td"):
                
                for span in td1.find_all("span"):
                    newrow1 = []
                    newrow1.append(span.text.replace('\n', ' ').strip())
                    table_data_m.append(newrow1)


    for table in x.find_all("table")[1:]:
        for tr in table.find_all("tr"):
            newrow = []
            for td in tr.find_all("td"):
                newrow.append(td.text.replace('\n', ' ').strip())
            table_data_m.append(newrow)

    df = pd.DataFrame(table_data_m)
    sheetname = 'Sheet%s' % counter
    if(counter!=1):
        writer.book = load_workbook(path)
    df.to_excel(writer, sheet_name=sheetname)
    
    counter = counter + 1
    writer.save()