''' https://www.youtube.com/watch?v=g9flPDG9nnY
 
 Networking: Web Scraping or Web Spiderin (what you would do with a 
web page once you´ve retrieved it: extract the links from the web page
making a queue of in-retrieved links and then moving on
'''
# I did: pip install beautifulsoup4  | pip list

''' urlinks.py coud be a godd name for this file'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
if len(url) < 1: url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print(tags, type(tags), '\n')
for tag in tags:
    print(tag.get('href', None))
print()

# TCP/IP (particulary TCP) give us pipes/sockets btwn apps.
# Apps protocols are design to make use of these pipes
# HyperText Transfer Protocol is simple & powerful
# Py has good support for sockets. HTTP & HTML parsing