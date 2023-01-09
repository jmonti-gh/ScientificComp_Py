''' Chap #16 Retrieving and Vizualizing Data: 16-Viz C | Geodata '''

''' Data was crawled and resides in DB ...\PortableGit\geodat_aux
-- simple DB result of spidering process --
Now we are going to show the data en a map ¿? '''

''' Code & aux_data like where.data: https://www.py4e.com/code3/geodata.zip'''

import sqlite3
import json
import codecs

# connect to DB & mk cur obj. to execute SQL commands to it
conn = sqlite3.connect('../../../geodat_aux/geodata.sqlite')
cur = conn.cursor()

# get all the Locations table
cur.execute('SELECT * FROM Locations')
# open a file handle as utf-8, cause is utf-8 (codecs mod ¿?)
fh = codecs.open('../../../geodat_aux/where.js', 'w', 'utf-8')
# write first line of the JSON file i will create
fh.write('myData = [\n')
cnt = 0
for row in cur:     # for e/row in Locations table
    # row[0]: location or address and [1] contains the geodata
    # we have to decode the geodata
    data = str(row[1].decode())
    # parse the data en row[1]
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK'): continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        cnt += 1
        if cnt > 1 : fh.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fh.write(output)
    except:
        continue

fh.write("\n];\n")
cur.close()
fh.close()
print(cnt, "records written to where.js")
print("Open where.html to view the data in a browser")



