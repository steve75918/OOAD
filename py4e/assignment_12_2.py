# Do [cnt] find [pos] href and follow
# test url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# get input from user
url = input('Enter URL:')
cnt = int(input('Enter count:'))
pos = int(input('Enter position:'))

for x in range(cnt + 1):
    # print current url
    print('Retrieving:', url)

    # get html content
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # # change url for next time, note that position of list start from 0
    url = soup('a')[pos - 1].get('href')