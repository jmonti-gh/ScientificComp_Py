''' Scientific Computing w/Python - Budget App'''

# https://realpython.com/sort-python-dictionary/#:~:text=Sorting%20Dictionaries%20in%20Python%201%20Using%20the%20sorted,...%206%20Converting%20Back%20to%20a%20Dictionary%20
# https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6

# budget_v6.py                  # return string (bar chart) by the funct
# budget: presupuesto, balance: saldo, ledger: libro mayor

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
        if self.check_founds(amount):
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
        if self.check_founds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': 'Transfer to ' + obj.name})
            self.__blnc -= amount       # update balance substracting amount
            obj.deposit(amount, 'Transfer from ' + self.name )
            return True
        else: return False

    # Returns False if the amount is greater than the balance and True otherwise.
    def check_founds(self, amount):
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


def create_spend_chart(catlst):
    ''' Takes a list of categories as an argument, return a string that is a bar chart.
    The chart show the percentage spent in each category passed in to the function '''

    # Begin the strin-to-return (ret_str) with title as first ln 
    ret_str = 'Percentage spent by category \n' 
    #print('Percentage spent by category')

    # Calc. e/cat wthdrs sum and store in a dict. Then sum(di.values()), for big_total.
    di = {}
    for cat in catlst:
        tot_w_cat = 0
        for wd in cat.ledger:
            if wd['amount'] < 0:            # only wthdrs are less than 0 
                tot_w_cat += -wd['amount']  # chg sign cause aoriginal is neg.
        di[cat.name] = tot_w_cat            # Add results to di (still not %)
    #print(di, ' - ', sum(di.values()))
    
    # Calc the required % (rounded to nearest 10) and store in the same dict.
    big_tot = sum(di.values())
    for k in di:
        di[k] = round((di[k] * 100 / big_tot) / 10) * 10
    #print(di, ' - ', sum(di.values()))
    
    # New dic with reverse sort values, py ver3.7 dic t alre oreder collections
    rovals = sorted(di.values(), reverse=True)  # list of all vals reversed sorted
    diro = {}
    for val in rovals:
        for k in di:
            if di[k] == val: diro[k] = di[k]    # same key, same val, reverse-sort
    #print(diro, ' - ', sum(diro.values()))

    # Finished prev. calcs begin writing the char in the string
    # mk the top part of the chart
    for i in range(100, -1, -10):
        #print('{:>3}|'.format(i), end=' ')
        ret_str += '{:>3}| '.format(i)
        for j in diro.values():
            if i <= j:
                #print('o', end='  ')
                ret_str += 'o  '
        ret_str += '\n'

    # horizontal line below the bars should go two spaces past the final bar
    hlnlnght = 1 + len(catlst) * 3
    hln = ' ' * 4 + '-' * hlnlnght
    #print(hln)
    ret_str += hln + '\n'

    # Each category name should be written vertically below the bar
    # calc max lenght cat.name
    mxcatnm = 0
    for cat in diro:
        if len(cat) > mxcatnm: mxcatnm = len(cat)
    # write the cat names
    for i in range(mxcatnm):
        #print(' ' * 5, end='')
        ret_str += ' ' * 5
        for cat in diro:
            try:
                #print(cat[i], end='  ')
                ret_str += cat[i] + '  '
            except IndexError:
                #print(' ', end='  ')
                ret_str += ' ' * 3
                #ret_str += '   '
        #print()
        ret_str += '\n'

    return ret_str

fo = Category('Food')
clo = Category('Clothing')
aut = Category('Auto')

fo.deposit(1000, 'initial deposit')
fo.withdraw(10.15, 'groceries')
fo.withdraw(15.89, 'restaurant and mode foodnessty')
fo.transfer(50, clo)

clo.withdraw(9.67789, 'Taxes')
clo.transfer(20, aut)

aut.withdraw(16.0678723, 'Adueded takes and extra charges for late pay')
aut.transfer(2.5, clo)

ent = Category('Entertainment')
ent.deposit(200, 'initial deposit')
ent.withdraw(17, 'Bowling night')

print()
print(fo)
print()
print(create_spend_chart([aut, fo, ent, clo]))



            
# fo = Category('food')
# clo = Category('clothing')
# aut = Category('Auto')

# fo.deposit(1000, 'initial deposit')
# fo.withdraw(10.15, 'groceries')
# fo.withdraw(15.89, 'restaurant and mode foodnessty')
# fo.transfer(34, clo)

# clo.withdraw(13.67789, 'Taxes')
# clo.transfer(20, aut)
# clo.deposit(370, 'Rent debt collection')
# clo.withdraw(63.79, 'Debt payment')

# aut.withdraw(16.0678723, 'Adueded takes and extra charges for late pay')
# aut.transfer(1.5, clo)

# create_spend_chart([fo, clo, aut])

#print(aut)