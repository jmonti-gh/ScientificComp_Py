''' https://www.youtube.com/watch?v=EhQxwzyT16E '''

# Chapter 9 - tuples

t = (1,2,3,4)
print(max(t))
print(sorted(t, reverse=True))
# print(d)
# print(d.keys(), type(d.keys()))
# print(list(d))
# print(d.values(), type(d.values()))
# print(list(d.values()))
# print(d.items(), type(d.items()))
# print(list(d.items()))
print()

# mk a while-True + try-except only to assure correct fh
while True:
    try:
        sfn = input('Enter a file name:  ')
        if len(sfn) < 1: sfn = 'clown.txt'
        fh = open(sfn)
        #print(fh)
        break
    except IOError as e:
        print(e)
        print('Invalid file name, try again...')
    
# main (suppose fh is corrected open)
# count e/word an store result in d{}
clns, cwds, d = 0, 0, {}
for line in fh:     # for e/line of the file
    clns += 1
    wds = line.split()
    for wd in wds:  # for e/word of the line
        cwds += 1
        # create/retrieve/update value (conunt)
        d[wd] = d.get(wd, 0) + 1
        # .get, if key don't exist the value = 0 (default)

# # gor d{} i can print it
# print()
# print(d)
# print()

# Print 10 most repeated words
# first make a reversed order list (lst) by values (count)
# using list comprenhension & flipping k,v to v,k in interns tuples
lst = sorted([(v,k) for k,v in d.items()], reverse=True)
# 2d print de most repeated words in desd order
for v, k in lst[:5]:
    print(k, v, ' - or:', v, k)

# And... ALL IN ONE LINE
print('\n',sorted([(v, k) for k,v in d.items()][:5], reverse=True))

print()
print([ i*i for i in range(10)][:4])
# # obtain the most repeated word
# # now we want to find the most common word
# mcnt, mword = 0, ''
# for wd in d:
#     if d[wd] > mcnt:
#         mcnt = d[wd]
#         mword = wd

# print(mword, mcnt)
# print('Total lns:', clns, ' - tot words:', cwds, 
#     ' - tot. diff words:', len(d))