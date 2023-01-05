''' https://apipheny.io/free-api/ '''

# jokejson - Public Free Officel Joke API
import urllib.request, urllib.parse, urllib.error
import json

# for only one joke: https://github.com/15Dkatz/official_joke_api
url = 'https://official-joke-api.appspot.com/jokes/random'

# open url
uh = urllib.request.urlopen(url)
# read an decode data (string w/ JSON content)
data = uh.read().decode()
print('\nRetrived', len(data), 'characters\n')
print(data, type(data),'\n')

# get in JSON in Py as (dict o lst, this case dict) 
try:
    js = json.loads(data)
    print(js, type(js), '\n')
except:
    js = None
if not js:
    print('=== Failure To Retrieve ===')
    print(data)

# Print JSON content as usful program info
print(js['setup'])
a = input('      press Enter...')
print(js['punchline'], '\n')

   



srvcurl = 'https://official-joke-api.appspot.com/jokes/'
# while True:
#     while True:
#         joke = input("Enter, 'one', 'ten', 'type', 'exit':  ").lower()
#         if joke == 'one':
#             jktype = 'random'
#             break
#         elif joke == 'ten':
#             jktype = 'ten'
#             break
#         elif joke == 'type':
#             print('Future work')
#             break
#         elif joke == 'exit': break
#         else: print('Invalid input. Try again...')

#     if joke == 'exit': 
#         print('See you...')
#         break

#     url = srvcurl + jktype
#     #url = srvcurl + urllib.parse.urlencode({'address': address})

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrived', len(data), 'characters')

#     try:
#         js = json.loads(data)
#     except:
#         js = None
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('=== Failure To Retrieve ===')
#         print(data)
#         continue

# setup = js["setup"]
# punchln = js["punchline"]

# print(setup)
# a = input('Press enter...')
# print(punchln, '\n')

