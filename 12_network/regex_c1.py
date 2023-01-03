''' Regular Expressions: Practical Applications '''

# String parsings examples: Max & Min Spam Condidence (all w/regex)
import re

print()
while True:
    try:
        fn = input('Enter mbox filename:  ')
        if len(fn) < 1: fn = 'mbox_jm.txt'
        fh = open(fn)
    except OSError as e:
        print(e, '.  Try again...', sep='')
    else:
        numlst = []
        for ln in fh:
            #stf = re.findall('.*-Confidence: ([0-9.]+)', ln)
            stf = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', ln)
            if len(stf) != 1: continue
            numlst.append(float(stf[0]))
        print(sorted(numlst), ' - Min:', min(numlst), '- Max:', max(numlst))
        fh.close()
        break

# Other way... (less cpu work¿?)
print()
while True:
    try:
        fn = input('Enter mbox filename:  ')
        if len(fn) < 1: fn = 'mbox_jm.txt'
        fh = open(fn)
    except OSError as e:
        print(e, '.  Try again...', sep='')
    else:
        numlst = []
        for ln in fh:
            if re.search('^X-DSPAM-Confidence: [0-9.]+$', ln):
                stf = re.findall('[0-9.]+', ln)
                numlst.append(float(stf[0]))
        print(sorted(numlst), ' - Min:', min(numlst), '- Max:', max(numlst))
        fh.close()
        break

# Escape character: '\'
print()
x = 'We recieved $50.00 for focaccia'
y = re.findall('\$[0-9.]+', x); print(y)    # ['$50.00']
# .....
y = re.findall('\$[0-9.]+?', x); print(y)   # ['$5']
y = re.findall('\$[0-9.]', x); print(y)     # ['$5']
y = re.findall('\$[0-9.]*', x); print(y)    # ['$50.00']