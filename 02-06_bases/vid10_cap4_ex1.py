''' https://www.youtube.com/watch?v=ksvGhDsjtpw '''

def computepay(hours, rate):
    pass

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


