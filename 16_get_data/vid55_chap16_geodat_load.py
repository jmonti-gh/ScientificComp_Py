''' Chap #16 Retrieving and Vizualizing Data: 16-Viz C | Geodata '''

''' A Web crawler, sometimes called a spider or spiderbot and often
shortened to crawler, is an Internet bot that systematically browses the 
World Wide Web and that is typically operated by search engines for the 
purpose of Web indexing (web spidering)'''

''' Code & aux_data like where.data: https://www.py4e.com/code3/geodata.zip'''

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# if u have a Google Places API_k, enter here: api_key = 'aJM__oThk'

if api_key is False:
    api_key = 42
    srvcurl = "http://py4e-data.dr-chuck.net/json?"
else:
    srvcurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Add for urllib: http.client.HTTPConnection.debuglevel = 1

# JM test to acces the subdir selected to store data en SQLite db files
fh = open('../../../geodat_aux/geo_jm.txt', 'w')
fh.write('srvcurl = "http://py4e-data.dr-chuck.net/json?"')
fh.close()

# we're gonna make de DB or connecto to it if exists
conn = sqlite3.connect('../../../geodat_aux/geodata.sqlite')
cur = conn.cursor()
# we're gonna to create 'Locations' table if not exists
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Cause Py doesn't ship w/any legitimate certificates we have to 
# sort of Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# I open the file containing the places i want to look for
fh = open('../../../geodat_aux/where.data')
cnt = 0
for ln in fh:
    # To read only a bunch of 200 each time
    if cnt > 200:
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = ln.strip()
    print('')
    # I do a SELECT & pull out of DB that address
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", 
        (memoryview(address.encode()), ))
    # if it's is already in de DB we don't want to do it

    try:
        data = cur.fetchone()[0]
        print('Found in database', address)
        continue
    except:
        pass
        # if try block fail don't blow up and just do a pass and cont.

    parms = {}
    parms['query'] = address
    if api_key is not False: parms['key'] = api_key
    url = srvcurl + urllib.parse.urlencode(parms)

    print('Retriving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    cnt = cnt + 1

    try:
        js = json.loads(data)
    except:
        print(data)
        continue        # continue w/next line
    
    # if json is not ok break the for ln in fh loop
    if 'status' not in js or (js['status'] != 'OK' and 
        js['status'] != 'ZERO_RESULTS'):
        print(' ===== Failure TO Retrieve =====')
        print(data)
        break

    # if everything ok put data en DB
    cur.execute('INSERT INTO Locations (address, geodata) VALUES ( ?, ?)', 
        (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()   # must commit the insert to save permanently en DB
    if cnt % 10 == 0:       # e/10 lines make a 5 seconds pause to ¿?
        print('Pausing for a bit...')
        time.sleep(5)

# when finish the for ln in fh loop....
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

    
    







    



