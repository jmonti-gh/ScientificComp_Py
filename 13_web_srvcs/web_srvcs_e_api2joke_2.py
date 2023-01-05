''' https://apipheny.io/free-api/ '''

# jokejson - Public Free Officel Joke API
# https://github.com/15Dkatz/official_joke_api
import urllib.request, urllib.parse, urllib.error
import json
from time import sleep
from random import choice

def get_json(opt):
    url = srvcurl + opt
    #print(url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    try:
        js = json.loads(data)
        return js
    except:
        js = None
    if not js:
        print('=== Failure To Retrieve ===')
        print(data)

def one(ty=''):
    js = get_json(ty + 'random')
    print('\n', js['setup'])
    a = input('      press Enter...')
    print(js['punchline'], '\n')

def ten(ty=''):
    js = get_json(ty + 'ten')
    #print(js, type(js))
    # for it in js:
    #     print('\n', it['setup'])
    #     print(it['punchline'])
    for i in range(len(js)):
        print('\n', i+1, '.-  ', js[i]['setup'], sep='')
        print(js[i]['punchline'])

srvcurl = 'https://official-joke-api.appspot.com/jokes/'

while True:
    while True:
        joke = input("\nEnter, 'one', 'ten', 'prg', 'exit':  ").lower()
        if joke == 'one':
            one()
            break
        elif joke == 'ten':
            ten()
            break
        elif joke == 'prg':
            ten('programming/')
            break
        elif joke == 'exit': break
        else: print('Invalid input. Try again...')
    
    if joke == 'exit':
        lst = ['Smell you later', 'Argentina Campeón del Mundo', 
        'Siamo fouri', 'Catch you later', 'Keep in touch', 'Bye Bye',
        'Hasta la vista Baybe', 'Take it easy', 'Peace out']
        bye = choice(lst)
        print('\n', bye, '...\n', sep='')
        break

    # ver _3 w/cli args and help for use like HTTPresponse