''' Using re.search() like .find() '''

print('\n~~~~~ Any place in the ln,  using trin.find() method ~~~~~')
for ln in open('mbox_jm.txt'):
    ln = ln.rstrip()     # it's a new ln wo/last \n.
    if ln.find('From:') >= 0:
        print(ln)

print('\n~~~~~ Any place in the ln, using re.search() function ~~~~~')
import re
for ln in open('mbox_jm.txt'):
    ln = ln.rstrip()
    if re.search('From:', ln):
        print(ln)


''' Using re.search like startswith'''

print('\n~~~ At the begining of ln, using .startswith() method ~~~')
for ln in open('mbox_jm.txt'):
    ln = ln.rstrip()     # it's a new ln wo/last \n.
    if ln.startswith('From:'):
        print(ln)

print("\n~~~ At the begining ln, using re.search('^...'') function ~~~")
import re
for ln in open('mbox_jm.txt'):
    ln = ln.rstrip()
    if re.search('^From:', ln):
        print(ln)