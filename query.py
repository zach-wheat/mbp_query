import requests
from bs4 import BeautifulSoup


def landingpage_query(attempts=3):

    url = 'https://www.apple.com/shop/refurbished/mac/macbook-pro'
    #enter model to search
    model = 'Refurbished 16-inch'

    headers = {'user-agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/73.0.3683.86 Safari/537.36'}

    while attempts != 0:
        try:
            r = requests.get(url, headers=headers, timeout=15)
            attempts = 0
        except Exception as Ex:
            print(f'Error when retrieving landing page links: {Ex}')
            attempts -= 1
            print(f'Trying again. Number of attempts remaining: {attempts}')

    soup = BeautifulSoup(r.content, 'html.parser')
    products = soup.find_all('div', class_="refurbished-category-grid-no-js")

    urls = []
    for prod in products:
        for link in prod.findAll('a', href=True):
            for chunk in link:
                if model in chunk:
                    urls.append('https://www.apple.com' + link['href'])

    return urls
