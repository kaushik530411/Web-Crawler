import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page='+str(page)+'&q=Phones&viewType=grid'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')
        for link in soup.findAll('a',{'class' : '_2cLu-l'}):
            href = 'https://www.flipkart.com' + link.get('href')
            title = link.string
            # print(title)
            print(href)
            # get_single_data_item(href)
            # print()

        page += 1

def get_single_data_item(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for item_name in soup.findAll('div', {'class': '_1vC4OE _37U4_g'}): # Printing Price
        name = item_name.get_text(strip=True)  # extracting the texts from <react-text> when they are not stored in the variable
        print(name)
    for link in soup.findAll('a'):
        href = 'https://www.flipkart.com' + link.get('href')
        print(href)

trade_spider(3)

