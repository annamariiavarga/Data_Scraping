from requests import get
from bs4 import BeautifulSoup
import re
URL = "https://lnu.edu.ua/about/faculties/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "lab1.txt"
regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.text, 'lxml')
arr = []
with open('./links.txt', 'w') as file:
    for link in soup.find_all('a'):
        if link.get('href') is not None:
            if link.get('href') not in arr:
                if regex.match(link.get('href')):
                    file.write("link: {0}\n".format(link.get('href')))
                    arr.append(link.get('href'))
    for link in arr:
        URL = link
        page = get(URL, headers=HEADERS)
        soup = BeautifulSoup(page.text, 'lxml')
        for newlink in soup.find_all('a'):
            if newlink.get('href') is not None:
                if newlink.get('href') not in arr:
                    if regex.match(newlink.get('href')): 
                        file.write("link: {0}\n".format(newlink.get('href')))
                        arr.append(newlink.get('href'))


     