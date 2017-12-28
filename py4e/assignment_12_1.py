import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# get all span
print(sum([int(s.string) for s in soup('span')]))