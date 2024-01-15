import json
import requests
import re
from bs4 import BeautifulSoup


###############################################################
######### LET'S GET SOME INFO FROM GUIDO GITHUB PAGE ##########
###############################################################


URL = 'https://github.com/{}'
target = 'gvanrossum'
params = {'tab':'repositories'}
res = requests.get(url=URL.format(target), params=params)
bs_content = BeautifulSoup(res.text, 'html.parser')

repos = bs_content.find(id='user-repositories-list') \
                    .select('ul > li')
info = []
def main():
    for rep in repos:
        rep_name = rep.find('h3').get_text(strip=True)
        
        rep_description = rep.find('p', attrs={'itemprop':'description'})
        description = rep_description.get_text(strip=True) if rep_description else None

        rep_lang = rep.find('span', attrs={'itemprop':'programmingLanguage'})
        lang = rep_lang.get_text(strip=True) if rep_lang else None
        stars = rep.find('a', attrs={"href": re.compile('\/stargazers')})
        star = stars.get_text(strip=True) if rep_lang else "0"

        info.append({
            'repository': rep_name,
            'description': description,
            'language': lang,
            'stars' : star
        })

    with open('no_scrapy/guido_repos_info.json', 'w') as f:
        json.dump(info, f, indent=4)

if __name__ == "__main__":
    main()

    