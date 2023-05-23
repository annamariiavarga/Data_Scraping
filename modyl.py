import requests
from bs4 import BeautifulSoup
import csv


BASE_URL = "https://ek.ua/"
URL = f"{BASE_URL}/ua/mobile/universalnye-batarei/"
def scrape_powerbanks(\page_url):
response = requests.get(page_url)
soup = BeautifulSoup(response.text, 'html.parser')
powerbanks = soup.find_all('div', class_='model-short-div')
data = []
    for powerbank in powerbanks:
        model = powerbank.find('div', class_='model-short-title').text.strip()
        image_url = powerbank.find('img')['src']
        shop = powerbank.find('a', class_='shop_name').text.strip()
        price = powerbank.find('div', class_='model-price-range').text.strip()
         data.append([model, image_url, shop, price])
        return data


def scrape_all_powerbanks():
base_url='https://ek.ua'
    page_url = base_url + '/list/7a3/'
    data = []
 while True:
    page_data = scrape_powerbanks (page_url)
        data.extend(page_data)

        next_page_link = soup.find('a', class_='g-pagination-next')
        if not next_page_link:
            break
        page_url = base_url + next_page_link['href']

with open('powerbank_offers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Model', 'Image URL', 'Shop', 'Price'])
    writer.writerows(data)

print("Дані про пропозиції PowerBank зібрано та збережено у файл powerbank_offers.csv")





