import json
import requests
from bs4 import BeautifulSoup


#############################################################
######## LOGING PROCESS BY CREATING REQUEST SESSION #########
#############################################################


URL = 'https://github.com/{}'
username = 'farshad-panahi'

session = requests.Session()
res = session.get(url=URL.format('login'))

bs_content = BeautifulSoup(res.text, 'html.parser')


credentials = {}

for form in bs_content.find_all('form'):
    for inputs in form.select('input[type=hidden]'):
        credentials[inputs.get('name')] = inputs.get('value')

credentials.update({
    username: '$',
})

res = session.post(url=URL.format('session'), data=credentials)
print(1, res.url)

payloads = {'tab': 'repositories'}
res = session.get(url=URL.format(username),params=payloads)
print(2, res.url)
profile = BeautifulSoup(res.text, 'html.parser')

info=profile.find('div', class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
info = info.get_text(strip=True)
print(3, info)

#https://github.com/session
#https://github.com/farshad-panahi?tab=repositories
#An Iranian Adventurer
