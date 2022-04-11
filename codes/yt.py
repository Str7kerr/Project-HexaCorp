from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import pandas as pd

url = "http://millenniumcricketleague.com/Home/Results.aspx?tt=1"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

league_table = soup.find_all('table' , class_ = 'GridViewStyle')[2]

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td').text.strip()
        pl_col =  row.find_all('td')
        print(pl_team)