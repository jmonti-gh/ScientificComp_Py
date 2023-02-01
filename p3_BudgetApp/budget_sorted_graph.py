''' Scientific Computing w/Python - Budget App'''

# JM ver. change from the required in two points:
# 1. Mk a graphs orderer from higher to lower %, not for order of list cats pass to the funct.
# 2. The height of each bar is rounded to the nearest 10, not rounded DOWN to nearest 10.

class Category:
    def __init__ (self, category):
        self.name = category
        self.ledger = []        # instance variable called ledger that is a list
        self.__blnc = 0         # to store the balance on the fly       

    # Register a deposit in ledger[] & update balance
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.__blnc += amount           # update balance adding amount

    # Register a withdraw in ledger[] (chge amount to neg before) & update balance
    # & return True, if enough founds, else do nothing and return False.
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': description})
            self.__blnc -= amount       # update balance substracting amount
            return True
        else: return False

    # Returns current balance of the budget cat, based on deps & wthdrs occurred. 
    def get_balance(self):
        return self.__blnc

    # Add a wthdr & add a dep to the other cat & update balance & return Tue if
    # enough founds, else do nothing and return False.
    def transfer(self, amount, obj):
        if self.check_funds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': 'Transfer to ' + obj.name})
            self.__blnc -= amount       # update balance substracting amount
            obj.deposit(amount, 'Transfer from ' + self.name )
            return True
        else: return False

    # Returns False if the amount is greater than the balance and True otherwise.
    def check_funds(self, amount):
        if amount > self.__blnc: return False
        else: return True

    # To display when budget object is printed
    def __str__(self):
        ret_str = self.name.center(30, '*') + '\n'
        for el in self.ledger:
           ret_str += ('{:<23}{:>7.2f}'.format(el['description'][:23],
                        el['amount']) +'\n') 
        ret_str += 'Total: ' + str(self.get_balance())
        return ret_str


def create_spend_chart(categories):
    ''' Takes a list of categories as an argument, return a string that is a bar chart.
    The chart show the percentage spent in each category passed in to the function '''

    # Initialize the string-to-return (ret_str) with title as first line
    ret_str = 'Percentage spent by category\n' 

    # Calc. e/cat wthdrs sum and store in a dict. Then sum(di.values()), for big_total.
    di = {}
    for cat in categories:
        tot_w_cat = 0
        for wd in cat.ledger:
            if wd['amount'] < 0:            # only wthdrs are less than 0 
                tot_w_cat += -wd['amount']  # chg sign cause aoriginal is neg.
        di[cat.name] = tot_w_cat            # Add results to di (still not %)
    
    # Calc the required % (rounded to nearest 10) and store in the same dict.
    big_tot = sum(di.values())
    for k in di:
        di[k] = round((di[k] * 100 / big_tot) / 10) * 10

    # Reverse sort the dict by value
    di = dict(sorted(di.items(), key = lambda itm: itm[1], reverse=True))
    ''' sorted(iter, key=None, reverse=False): key specifies a function of one arg
    that is used to extract a comparison key from each element in iterable (for 
    example, key=str.lower). -> python.org - documentation - library. '''

    ## Finished calcs needed, continue writing the char in the string
    # mk the top part of the chart
    for i in range(100, -1, -10):
        ret_str += '{:>3}| '.format(i)
        for j in di.values():
            if i <= j:
                ret_str += 'o  '
            else:
                ret_str += ' ' * 3
        ret_str += '\n'

    # horizontal line below the bars should go two spaces past the final bar
    hlnlnght = 1 + len(categories) * 3  # int: first '-' sep y_axis & add 3 more f/e/cat
    ret_str += ' ' * 4 + '-' * hlnlnght + '\n'

    ##  Each category name should be written vertically below the bar
    mxcatnm = max(map(lambda x: len(x), di))    # max cat name length 
    for i in range(mxcatnm):              
        ret_str += ' ' * 5
        for cat in di:
            try:
                ret_str += cat[i] + '  '    # write cat name char + 2 spaces
            except IndexError:
                ret_str += ' ' * 3          # no more chars in cat name
        if i < mxcatnm - 1: ret_str += '\n'

    return ret_str

fo = Category('Food')
clo = Category('Clothing')
aut = Category('Auto')

fo.deposit(1000, 'initial deposit')
fo.withdraw(10.15, 'groceries')
fo.withdraw(15.89, 'restaurant and mode foodnessty')
fo.transfer(50, clo)

clo.withdraw(25.55)

aut.deposit(120, 'Initial deposit')
aut.withdraw(14.9678723, 'Adueded takes and extra charges for late pay')

print(fo)
print(clo)
print(create_spend_chart([aut, fo, clo]))
