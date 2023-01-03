''' Matching and Extracting Data  '''
# re.findall('regex', trin), return a list of zero o more sub-trin
import re
x = 'My 2 favorites numbers are 34 & 97'
y = re.findall('[0-9]', x); print(y)
y = re.findall('[0-9]+', x); print(y)
y = re.findall('[0-9]*', x); print(y)
y = re.findall('[AEIOU]+', x); print(y)

print("\n~~~ Greedy Marching: re.findall('^F.+:', x) ~~~")
x = 'From: Using the: char: chr(93)'
y = re.findall('^F.+:', x)  # Greedy (the larger of all)
print(y)                    # ['From: Using the: char:']
print("\n~~~ NON-Greedy Marching: re.findall('^F.+?:', x) ~~~")
y = re.findall('^F.+?:', x) # non-greedy (the first)
print(y)                    # ['From:']    

# Fine-Tuning
print()
x = 'From gordo.hor@mtm.com.ar Sat Jan  5 09:14'
#x = 'From one gordo.hor@mtm.com.ar Sat Jan  5 09:14' -OJO
y = re.findall('\S+@\S+', x); print(y)          # ['gordo.hor@mtm.com.ar']
# Perentheses ( Start extrac and ) End extract:
y = re.findall('^From (\S+@\S+)', x); print(y)  # ['gordo.hor@mtm.com.ar']

print()
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)                                  # ['csev@umich.edu', 'cwen@iupui.edu']
l = re.findall('\S+@\S+', s); print(l)      # ['csev@umich.edu', 'cwen@iupui.edu']
l = re.findall('\\\S+@\\\S+', s); print(l)      # []
l = re.findall('\\\\S+@\\\\S+', s); print(l)    # []