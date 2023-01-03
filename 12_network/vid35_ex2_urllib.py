''' 
Networking: using urllib in Python, a library that does
all the socket work for us & mks web pages look like files'''

# urllib is a pkg that collects several mods for work w/URLs
# urllib.request: for opening and reading URLs
# urllib. parse: for parsing URLs
# urllib.error: contain exceptions rised by .request
import urllib.request, urllib.parse, urllib.error

# .urlopen funct. does all for as: makes the connection, does the get,
# encodes the get request, retrieve at this moment, retrieves all the 
# headers and keeps it for you for later & returns an object
shand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Reading a text file
print("\n\turllib.request.urlopen('http://data.pr4e.org/romeo.txt'):")
print('-' * 70)
for ln in shand:
    # lines we get are bytes, we have to decode
    print('\t',ln.decode().strip())
shand.close()

# Counting words repeatance
print()
counts = dict()
for ln in urllib.request.urlopen('http://data.pr4e.org/romeo.txt'):
    wds = ln.decode().split()
    for wd in wds:
        counts[wd] = counts.get(wd, 0) + 1
# When finish 'for ln in ...' loop handle is automatic close
print(counts, ' - Max. repetead:', max(counts.values()))

# Reading Web Pages (HTML writed)
print("\n\turllib.request.urlopen('http://www.dr-chuck.com/page1.htm'):")
print('-' * 70)
for ln in urllib.request.urlopen('http://www.dr-chuck.com/page1.htm'):
    # lines we get are bytes, we have to decode
    print('\t',ln.decode().strip())
shand.close()

# Later Parssing HTML (a.k.a. Web Scraping)