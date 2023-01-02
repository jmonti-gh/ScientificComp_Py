''' https://www.youtube.com/watch?v=1bSqHot-KwE '''

trin = 'X-DSPAM-Confidence: 0.8475 '
colon_pos = trin.find(':')
snbr = trin[colon_pos + 1:]
print(snbr, type(snbr))
# blanks chars (' ' , tab, \n) don't bother
fnbr = float(snbr)
print(fnbr, type(fnbr))
print()
# more examples w/blanks
a = '   \n  \t    0.76   \n\t'
print(a, type(a))
b = float(a)
print(b, type(b))



