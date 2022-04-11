from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook
from pandas import Series, ExcelWriter

urls = ["http://millenniumcricketleague.com/Home/ShowTeam.aspx?tid=22", "http://millenniumcricketleague.com/Home/ShowTeam.aspx?tid=40"]
counter = 1
for url in urls:
    table_data = []
    final = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    x = soup.find_all('table')
    for table in x[1:]:
        for tr in table.find_all("tr"):
            newrow = []
            for td in tr.find_all("td"):
                newrow.append(td.text.replace('\n', ' ').strip())
            table_data.append(newrow)
    path = "F:\codes\meta_1.xlsx"
    writer1 = pd.ExcelWriter(path,engine='xlsxwriter')   
    df = pd.DataFrame(table_data)
    
#    sheet_name = 
    df.to_excel(writer1,'Sheetoo%s' % counter)
    writer1.save()
    print("Once!")
    counter = counter+1
    
    

writer1.close()
#    df.to_excel(writer,sheet_name='x1')
    
    
    # wb = Workbook()
    # ws = wb.create_sheet(title="IDLISAMBAR")

    #ws.append(t_headers)
    #for roww in table_data:
    #    row = [roww[0], roww[1], roww[2], roww[3], roww[4], roww[5], roww[6],
    #        roww[7]]
    #    ws.append(row)
    #wb.save('bhaisabyehkisslinemeinaagayeaap.xlsx')
