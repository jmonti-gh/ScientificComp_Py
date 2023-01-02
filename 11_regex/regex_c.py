''' Regular Expressions: Practical Applications '''



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
print(y)
print("\n~~~ NON-Greedy Marching: re.findall('^F.+?:', x) ~~~")
y = re.findall('^F.+?:', x)  # non-greedy (the first)
print(y)

# Fine-Tuning
print()
x = 'From gordo.horen@mtm.com.ar Sat Jan  5 09:14'
#x = 'From one gordo.horen@mtm.com.ar Sat Jan  5 09:14' -OJO
y = re.findall('\S+@\S+', x); print(y)
# Perentheses ( Start extrac and ) End extract:
y = re.findall('^From (\S+@\S+)', x); print(y)

print()
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
l = re.findall('\S+@\S+', s); print(l)