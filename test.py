import scholarly
import time
from googlesearch import search
import requests


class CustomSearchError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


start_time = time.time()
payload = {'key':'AIzaSyBcRhfxFn9Y3S-G63p-kApyTE9BhUmeBTA',
            'cx': '005251479122416850940:oiwjxnvfi00',
            'q': 'NPHS2 V260E Is a Frequent Cause of Steroid-Resistant Nephrotic Syndrome in Black South African Children'}
response = requests.get('https://www.googleapis.com/customsearch/v1/siterestrict', params=payload)
data = dict(response.json())
print(data)
if 'error' in data:
    raise CustomSearchError(data['error']['code'], data['error']['message'])
total = int(data['searchInformation']['totalResults'])
print(total)
if total > 0:
    article = data['items'][0]['link']
    print(article)
print((time.time() - start_time), 'seconds')


""" start_time = time.time()
url = next(search('pmid Multicohort genomewide association study reveals a new signal of protection against HIV-1 acquisition', num=1,stop=0))
print(url)
print((time.time() - start_time), 'seconds') """

"""start_time = time.time()
search_query = scholarly.search_author('sophie limou')
author = next(search_query).fill()
for pub in author.publications:
    url = next(search('pmid '+ pub.bib['title'], num=1,tld="co.in",stop=0))
    print(url)
print((time.time() - start_time), 'seconds')"""
