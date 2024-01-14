import re
import requests
from bs4 import BeautifulSoup
import json


URL = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
res = requests.get(url=URL)
content = BeautifulSoup(res.text, 'html.parser')

# cra

episods = []
all_episods_table=content.find_all("table", class_="wikitable plainrowheaders wikiepisodetable")

for table in all_episods_table:
    headers = []
    rows = table.find_all("tr")
    
    for header in table.find('tr').find_all('th'):
        cs = header.text.split()
        js = " ".join(cs)
        headers.append(js)

    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th', 'td']):
            cs=col.text.split()
            js=" ".join(cs)
            values.append(js)

        if values:
            episods_to_dict = {headers[i]:values[i] for i in range(len(values))}
            episods.append(episods_to_dict)


with open ('no_scrapy/got_table_info.json', 'w') as f:
    json.dump(episods, f)