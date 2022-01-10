import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.dcard.tw/f'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
decard_title = soup.find_all('hs',re.compile(()))