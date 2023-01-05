''' https://www.youtube.com/watch?v=TJGJN0T8tak '''

# http://g.co/dev/maps-no-account

'''{
   "error_message" : "You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account",
   "results" : [],
   "status" : "REQUEST_DENIED"
}
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
    
    print(json.dumps(js, ident=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng= js["results"][0]["geometry"]["location"]["lng"]
    print('lat:', lat, 'lng:', lng)
    location = js["results"][0]["formatted_address"]
    print(location)