from query import landingpage_query
from sub_query import subpage_query
import time
from datetime import datetime
import random
from twilio_alert import twilio


# Requests https://www.apple.com/shop/refurbished/mac/macbook-pro and checks to see if model year(s) \
# specified in sub_query are available. If so, Twilio notification containing link(s) is sent via text.


def main():
    print(f'Running job... Current time: {datetime.now()}')
    print('\n')
    urls = landingpage_query()
    print(f"Number of url's retrieved: {len(urls)}. Moving to subpage_query")

    output = []
    for url in urls:
        time.sleep(random.uniform(1.01, 3.77))
        try:
            link = subpage_query(url)
            if link:
                output.append(link)
                print(f'link found: {link}. Moving to next machine')
        except Exception as Ex:
            print(f'Error while crawling page: {url}. Exception: {Ex}')
            continue

    if output:
        print(f'Job completed: {datetime.now()}')
        outlist = ',\n\n'.join([link for link in output])
        print(f'Macbook query results: {outlist}')
        return twilio(f'Macbook query results: {outlist}')
    print(f'Job completed: {datetime.now()}')
    print('No Macbooks found for year(s) searched...')
    return twilio('No Macbooks found for selected year(s)...')


if __name__ == "__main__":
    main()


