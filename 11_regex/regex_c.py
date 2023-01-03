''' Regular Expressions: Practical Applications '''

# String parsings examples: extract hostname from mbox file

# Using strings method .find() & string slicing - base
data = 'From cho.chan@estan.com.ar Sun Oct  1 06:14'
atpos = data.find('@')          # find te position of first @
print('atpos:', atpos, end=' - ')
sppos = data.find(' ', atpos)   # find first space beginig search in atpos position
# or Find the position of first space from the first @
print('sppos:', sppos, end=' - ')
host = data[atpos + 1: sppos]   # up to but NOT included sppos char
print(host)

# From a file (+ string.startswith() method)
print()
while True:
    try:
        fn = input('Enter mbox filename:  ')
        if len(fn) < 1: fn = 'mbox_jm.txt'
        fh = open(fn)
    except OSError as e:
        print(e, '.  Try again...', sep='')
    else:
        cln = clnFrom = 0
        for ln in fh:
            cln += 1
            if not ln.startswith('From '): continue
            clnFrom += 1
            atpos = ln.find('@')          # find te position of first @
            sppos = ln.find(' ', atpos)   # find first space beginig search in atpos position
            host = ln[atpos + 1: sppos]   # up to but NOT included sppos char
            print(host)
        fh.close()
        break

# Using double split pattern (split returns list.)
print()
while True:
    try:
        fn = input('Enter mbox filename:  ')
        if len(fn) < 1: fn = 'mbox_jm.txt'
        fh = open(fn)
    except OSError as e:
        print(e, '.  Try again...', sep='')
    else:
        for ln in fh:
            if not ln.startswith('From '): continue
            words = ln.split()      # split terms usins spaces as delimters
            host = words[1].split('@')
            print(host[1])
        fh.close()
        break
    # here we known email es de 2d element in the ln.split() & hostname
    # is right after @ (of course this) -first elemnet of email addr-

# Using regex - first base one line-string
print()
import re
print(re.findall('@([^ ]*)', data))     # [^ ] non-blank char, * any number
print(re.findall('@(\S*)', data))       # \S == [^ ]
print(re.findall('^From .*@(\S*)', data))  # all cases one-item list  
#Using regex enterly file
while True:
    try:
        fn = input('Enter mbox filename:  ')
        if len(fn) < 1: fn = 'mbox_jm.txt'
        fh = open(fn)
    except OSError as e:
        print(e, '.  Try again...', sep='')
    else:
        for ln in fh:
            # host = re.findall('^From .*@(\S*)', ln)
            # if len(host) > 0: print(host)
            if re.search('^From .*@.*[0-9]+', ln):
            #if re.search('^From ', ln):
                print(re.findall('^From .*@(\S*)', ln))
        fh.close()
        break
    
# print()
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)
# l = re.findall('\S+@\S+', s); print(l)