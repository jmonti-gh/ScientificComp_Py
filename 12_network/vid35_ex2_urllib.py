''' https://www.youtube.com/watch?v=8yis2DvbBkI '''

import urllib.request, urllib.parse, urllib.error

shand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Reading a text file
print("\n\turllib.request.urlopen('http://data.pr4e.org/romeo.txt'):")
print('-' * 70)
for ln in shand:
    print('\t',ln.decode().strip())
shand.close()

# Counting the repetition of words
print()
counts = dict()
for ln in urllib.request.urlopen('http://data.pr4e.org/romeo.txt'):
    wds = ln.decode().split()
    for wd in wds:
        counts[wd] = counts.get(wd, 0) + 1
# When finish 'for ln in ...' loop handle is automatic close
print(counts, ' - Max. repetead:', max(counts.values()))