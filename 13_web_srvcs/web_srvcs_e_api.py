''' Web Services: APIs (Application Program Interface)
API specifies an interface and contros objs. specified in that iface
API is a contract: if you do this & this..., we are give you data this way
Soft that provides API´s functionality is the 'implementation' of the API
'''
# geojason 
import urllib.request, urllib.parse, urllib.error
import json

srvcurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = srvcurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

lat = js["results"][0]["geometry"]["location"]["lat"]
lng= js["results"][0]["geometry"]["location"]["lng"]
print('lat:', lat, 'lng:', lng)
location = js["results"][0]["formatted_address"]
print(location)



