from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.brainyquote.com/topics/music'
page = requests.get(url).text

soup = bs(page, 'lxml')
#  b-qt bg-auth
quotes = soup.find_all('a', {'class': 'b-qt'})
#author = quotes.find_next_siblings('a', {'class': 'bg-auth'})
#print(quotes)
#print(author)
Quote = {}
print(len(quotes))
for q in quotes:
    #print()
    auth = q.find_next_siblings('a')
    Q = q.string
    #print(auth[0].string)
    Quote.update({Q:auth[0].string})
    #print(f'by {q[1].string}')

#pprint(Quote)
for key, value in Quote.items():
    print(f'"{key}":"{value}",')