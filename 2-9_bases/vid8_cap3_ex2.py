''' https://www.youtube.com/watch?v=KJN3-7HH6yk '''

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
else:
    if hours > 40:
        # reg = hours * rate
        # ovt = (hours - 40) * rate * 0.5
        # pay = reg + ovt
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    print('Pay:', pay)
finally:
    print("That's all folks")


# # aux code to see identation (& output)
# print()
# for i in range(6):
#     print(i)
#     if i > 2:
#         print('Bigger than 2')
#     print('Done with i', i)
# print('All Done')

