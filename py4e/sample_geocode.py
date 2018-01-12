import urllib.parse
import urllib.error
import urllib.request
import json

# get data by google geocode
# send data by GET in json format
geocode_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    addr = input('Enter location: ')
    if len(addr) < 1:
        break

    # add paramter on url
    url = geocode_url + urllib.parse.urlencode({'address': addr})

    print('Retrieving:', url)
    geocode_result = urllib.request.urlopen(url).read().decode()

    print('Retrieved', len(geocode_result), 'characters')

    # analysis retrieved data
    try:
        data = json.loads(geocode_result)
    except Exception as e:
        data = None

    # verify data
    if (not data) or ("status" not in data) or (data['status'] != 'OK'):
        print('==== Failure To Retrive ====')
        print(data)
        continue

    # extract data and output
    geo_lat = data['results'][0]['geometry']['location']['lat']
    geo_lng = data['results'][0]['geometry']['location']['lng']
    print('Locate at lat:', geo_lat, ', lng:', geo_lng)

    f_addr = data['results'][0]['formatted_address']
    print('Full Address:', f_addr)
