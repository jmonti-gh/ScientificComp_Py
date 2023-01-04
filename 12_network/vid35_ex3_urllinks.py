''' https://www.youtube.com/watch?v=g9flPDG9nnY '''
# I did: pip install beautifulsoup4  | pip list

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# if the website to inspect have ssl
import ssl
# To ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url, context=ctx).read()    # if use ssl ingnore errs
# html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags (<a ... </a> ) ... & count it
tags = soup('a')
cnt = 0
for tag in tags:
    cnt +=  1
    print('{:>4}'.format(cnt), tag.get('href', None))
print('Total links founded:', len(tags), '  - chek w/cnt:', cnt)
print()

