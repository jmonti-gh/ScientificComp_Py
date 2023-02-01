''' Scientific Computing w/Python'''

# budget_v5.py                  # use of dicts in funct.
# budget: presupuesto, balance: saldo, ledger: libro mayor

class Category:
    def __init__ (self, category):
        self.name = category
        self.ledger = []        # ledger -> libro mayor
        self.__blnc = 0         # to store the balance on the fly       

    # Register a deposit in ledger[]
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.__blnc += amount       # update balance adding

    # Register a withdraw in ledger[] (chge amount to neg before)
    def withdraw(self, amount, description=''):
        if self.check_founds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': description})
            self.__blnc -= amount   # update balance substracting
            return True
        else: return False

    def get_balance(self):
        return self.__blnc

    def transfer(self, amount, obj):
        if self.check_founds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': 'Transfer to ' + obj.name})
            self.__blnc -= amount
            obj.deposit(amount, 'Transfer from ' + self.name )
            return True
        else: return False
        pass

    def check_founds(self, amount):
        if amount > self.__blnc: return False
        else: return True

    def __str__(self):
        ret_str = self.name.center(30, '*') + '\n'
        for el in self.ledger:
           ret_str += ('{:<23}{:>7.2f}'.format(el['description'][:23],
                        el['amount']) +'\n') 
        ret_str += 'Total: ' + str(self.get_balance())
        return ret_str


def create_spend_chart(catlst):
    # Takes a list of categories as an argument, return a string that is a bar chart.
    # The chart show the percentage spent in each category passed in to the function

    # Begin the returned string (ret_str) with title 
    #ret_str = 'Percentage spent by category \n'
    # 
    print('Percentage spent by category')

    # Calc. e/cat wthdrs sum and store in a dict. Then sum(di.values()), for big_total.
    di = {}
    for cat in catlst:
        tot_w_cat = 0
        for wd in cat.ledger:
            if wd['amount'] < 0:            # only wthdrs are less than 0 
                tot_w_cat += -wd['amount']  # chg sign cause aoriginal is neg.
        di[cat.name] = tot_w_cat            # Add results to di (still not %)
    print(di, ' - ', sum(di.values()))
    
    # Calc the required % (rounded to nearest 10) and store in the same dict, respective key
    big_tot = sum(di.values())
    for k in di:
        di[k] = round((di[k] * 100 / big_tot) / 10) * 10
    print(di, ' - ', sum(di.values()))

    # # mk a rev_ord_list from high to low in values
    # rev_ord_perct = sorted(di.values(), reverse=True)
    # rocats = []
    # for perct in rev_ord_perct:
    #     for k in di:
    #         if di[k] == perct: rocats.append(k)
    # print(rev_ord_perct, rocats)

    # New dic with everse sort values dict, py ver3.5 dic t alre oreder collections
    rovals = sorted(di.values(), reverse=True)  # list of all vals reversed sorted
    diro = {}
    for val in rovals:
        for k in di:
            if di[k] == val: diro[k] = di[k]    # same key, same val, reverse-sort
    print(diro, ' - ', sum(diro.values()))

    # mk the top part of the chart
    for i in range(100, -1, -10):
        print('{:>3}|'.format(i), end=' ')
        for j in diro.values():
            if i <= j:
                print('o', end='  ')
        print()

    # horizontal line below the bars should go two spaces past the final bar
    hlnlnght = 1 + len(catlst) * 3
    hln = ' ' * 4 + '-' * hlnlnght
    print(hln)

    # Each category name should be written vertically below the bar
    # calc max lenght cat.name
    mxcatnm = 0
    for cat in diro:
        if len(cat) > mxcatnm: mxcatnm = len(cat)
    # write the cat names
    for i in range(mxcatnm):
        print(' ' * 5, end='')
        for cat in diro:
            try:
                print(cat[i], end='  ')
            except IndexError:
                print(' ', end='  ')
        print()

fo = Category('Food')
clo = Category('Clothing')
aut = Category('Auto')

fo.deposit(1000, 'initial deposit')
fo.withdraw(10.15, 'groceries')
fo.withdraw(15.89, 'restaurant and mode foodnessty')
fo.transfer(50, clo)

clo.withdraw(13.67789, 'Taxes')
clo.transfer(20, aut)

aut.withdraw(16.0678723, 'Adueded takes and extra charges for late pay')
aut.transfer(2.5, clo)

create_spend_chart([aut, fo, clo])



            
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