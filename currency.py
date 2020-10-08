# script parses info about currency on google page through html elements

import requests
from bs4 import BeautifulSoup #for HTML
import time #for pausing program

USD_CAD = 'https://www.google.com/search?q=usd+to+cad&rlz=1C1CHBF_enCA884CA884&oq=ysd+to&aqs=chrome.1.69i57j0l7.2264j1j7&sourceid=chrome&ie=UTF-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

def check_currency():
    full_page = requests.get(USD_CAD, headers=headers)
# gets full information on the page
    soup = BeautifulSoup(full_page.content, 'html.parser')
# finds specific elements
    convert = soup.findAll('span', {'class': "DFlfde", 'class': 'SwHCTb', 'data-precision': 2})

    print('1 USD equals to: ' + convert[0].text + ' CAD')
# pauses program and calls it again
    time.sleep(5)
    check_currency()

print(check_currency())