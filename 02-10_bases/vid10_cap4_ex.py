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
except:
    print('Error, please enter numeric input')
else:
     print('Pay:', computepay(hs, rt))
finally:
    print("That's all folks")



