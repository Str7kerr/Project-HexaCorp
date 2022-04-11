from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import load_workbook
from pandas import Series, ExcelWriter

urls = ["http://millenniumcricketleague.com/Home/ShowTeam.aspx?tid=22",
        "http://millenniumcricketleague.com/Home/ShowTeam.aspx?tid=40"]
path = "F:\codes\meta_1.xlsx"
writer = pd.ExcelWriter(path,engine='openpyxl')
counter = 1
for url in urls:
    table_data_m = []
    
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    x = soup.find_all('table')
    for table in x[1:]:
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
    print("Once!")
    counter = counter + 1
    writer.save()