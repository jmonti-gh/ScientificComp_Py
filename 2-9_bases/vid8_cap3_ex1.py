''' https://www.youtube.com/watch?v=crLerB4ZxMI '''

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours > 40:
    # reg = hours * rate
    # ovt = (hours - 40) * rate * 0.5
    # pay = reg + ovt
    pay = 40 * rate + (hours - 40) * rate * 1.5
else:
    pay = hours * rate
print('Pay:', pay)




# # aux code to see identation (& output)
# print()
# for i in range(6):
#     print(i)
#     if i > 2:
#         print('Bigger than 2')
#     print('Done with i', i)
# print('All Done')

