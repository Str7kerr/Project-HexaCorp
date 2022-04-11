from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import pandas as pd

s = HTMLSession()
url = "http://millenniumcricketleague.com/Home/ShowTeam.aspx?tid=22"
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
        
    # final.append(table_data)
#print(final)


# for tr in x.find_all("tr"):
#     newrow = []
#     for td in tr.find_all("td"):
#         newrow.append(td.text.replace('\n', ' ').strip())      
#     table_data.append(newrow)
# final.append(table_data)      
#final.append(table_data)
    
    
#print(table_data)



#print(x.text.replace('\n',' ').strip())

# for itr in x[1:]:


df = pd.DataFrame(table_data)
df.to_excel('meta_stats8.xlsx')