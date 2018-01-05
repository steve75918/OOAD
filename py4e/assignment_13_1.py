import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print('Retrieving', url, '...')

api_ref = urllib.request.urlopen(url).read()

print('Retrived', len(api_ref), 'characters')

data = ET.fromstring(api_ref)

print('Count:', len(data.findall('.//count')))
print('Sum:', sum([int(x.text) for x in data.findall('.//count')]))
