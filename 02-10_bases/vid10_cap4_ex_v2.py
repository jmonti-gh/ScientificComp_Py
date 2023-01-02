''' https://www.youtube.com/watch?v=ksvGhDsjtpw '''

reghs = 40.00

def computepay(hours, rate):
    if hours > reghs:
        pay = reghs * rate + (hours - reghs) * rate * 1.5
    else:
        pay = hs * rate
    return round(pay, 2)

try:
    hs = float(input('Enter Hours: '))
    rt = float(input('Enter Rate: '))
    print('Pay:', computepay(hs, rt))
except ValueError:
    # I only know posiblle ValueError for both inputs and nothing
    # if another tyupe of Error is risen , then will be a Traceback
    print('Error, please enter numeric input')




