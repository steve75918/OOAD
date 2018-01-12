import urllib.parse
import urllib.error
import urllib.request
import json

def_service_url = 'http://py4e-data.dr-chuck.net/comments_40608.json'

p_url = input('Enter url: ')
if len(p_url) < 1:
    url = def_service_url
else:
    url = p_url

print('Retrieving:', url)
service_conn = urllib.request.urlopen(url)
service_result = service_conn.read().decode()

print('Retrieved', len(service_result), 'characters')

# analysis retrieved data
try:
    data = json.loads(service_result)
except Exception as e:
    data = None

# verify data
if (not data):
    print('==== Failure To Retrive ====')
    print(data)
    exit()

print(sum([int(x['count']) for x in data['comments']]))
