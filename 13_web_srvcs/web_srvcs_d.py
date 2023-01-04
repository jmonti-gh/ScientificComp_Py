''' Web Services: JSON (discovered by Douglas Crockford); JavaScript
Object Notationr, etresentes data as nested lists and dictionaruies
XML is better for rich & hierachical docs
JSON is best for just pulling data out an moving ir btwn two systems
'''

import json
print('\n~~~~~~~ JSON case: Nested dictionary & dictionary ~~~~~~~')
data = '''{
    "name" : "Martha",
    "phone" : {
        "type" : "intl",
        "number" : "+54 261 420 314"
    },
    "email" : {
        "hide" : "yes"
    }
} '''

info = json.loads(data)     # danger if errors en JSON input (data)
print(info, type(info))
print()
for k in info:
    print(k, ':',  info[k])
print('  email "hide" val:', info['email']['hide'], '\n')

# Another (maybe more complex) JSON
print('\n~~~~~~~ JSON case: Nested list & dictionary ~~~~~~~')
inpjson = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Quique"
    },
    {   "id" : "007",
        "x" : "9",
        "name" : "Pedro"
    },
    {   "id" : "052",
        "x" : "7",
        "name" : "Guille"
    }
]''' 

jsonin = json.loads(inpjson)    # Danger eg: Expecting ':' delimiter: line 3 column 13 (char 36)
print(jsonin, type(jsonin))
print()
for el in jsonin:
    print(el, type(el))
print()
print('{:^3}  {:^8}  {:^6}  {:^8}'.format('','--Name--', '--Id--', '--x attr--'))
cnt = 0
for it in jsonin:
    cnt += 1
    print('{:>3}   {:<8} {:>5}  {:>6}'.format(cnt, it['name'], it['id'],it['x']))
print()


# Another JSON
print('\n~~~~~~~ JSON case: dictionary & list ~~~~~~~')
x = """{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""
  
# parse x:
di = json.loads(x)
print(di, type(di))
print()
for k in di:
    print(k, ':',  di[k])
print('  Say one hobby:', di['Hobbies'][2], '\n')

