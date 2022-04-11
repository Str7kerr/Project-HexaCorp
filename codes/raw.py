
from openpyxl import Workbook
import pandas as pd
from bs4 import BeautifulSoup
import requests
url = "http://millenniumcricketleague.com/Home/Results.aspx?tt=1"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
x = soup.find_all('table', attrs={"class": "GridViewStyle"})[2]

data = {}
t_headers = []
for th in x.find_all("th"):
    t_headers.append(th.text.replace('\n', ' ').strip())
t_headers.append('Links')
table_data = []
table_data.append(t_headers)
#if False:

for tr in x.tbody.find_all("tr"):
    newrow = []
    urls = []
    for td in tr.find_all("td"):
        newrow.append(td.text.replace('\n', ' ').strip())
        
        for a in td.find_all('a',{"href":True}):
            urls.append(a['href'])
    for i in urls:
        newrow.append(i)
    
    table_data.append(newrow)
# print(table_data)

df = pd.DataFrame(table_data)
df.to_excel('total_stats2.xlsx')
    # newrow = []
    # url = []
    # for td in tr.find_all("td"):
    #     newrow.append(td.text.replace('\n', ' ').strip())
    #     for a in td.find_all('a', attrs={'class': 'Host'}):
    #         url.append(a['href'])
    #         break
    #     print(url)
#    newrow.append(url)
#    table_data.append(newrow)
#print(table_data)

#df = pd.DataFrame(table_data)
#df.to_excel('bhaisahab.xlsx')
#wb = Workbook()
#ws = wb.create_sheet(title="IDLISAMBAR")

#ws.append(t_headers)
#for roww in table_data:
#    row = [roww[0], roww[1], roww[2], roww[3], roww[4], roww[5], roww[6],
#        roww[7]]
#    ws.append(row)
#wb.save('bhaisabyehkisslinemeinaagayeaap.xlsx')