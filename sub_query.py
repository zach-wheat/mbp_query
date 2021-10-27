import requests
from bs4 import BeautifulSoup
import json


def subpage_query(url):

    headers = {'user-agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/73.0.3683.86 Safari/537.36'}

    r = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(r.content, 'html.parser')

    months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December', }
    #enter release year(s) to search
    years = {'2019', '2020'}

    data = json.loads(soup.find('script', type='application/ld+json').text)

    for month in months:
        for year in years:
            if f'Originally released {month} {year}' in data['description']:
                return data['url']


