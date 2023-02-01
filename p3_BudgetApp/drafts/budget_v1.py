''' Scientific Computing w/Python'''

# budget_v1.py                  # presupuesto

class Category:
    def __init__ (self, category):
        self.name = category
        self.ledger = []        # ledger -> libro mayor
        self.__blnc = 0         # calc. balance on the fly       

    # Register a deposit in ledger[]
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.__blnc += amount

    # Register a withdraw in ledger[] (chge amount to neg before)
    def withdraw(self, amount, description=''):
        if self.check_founds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': description})
            self.__blnc -= amount
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


def create_spend_chart(lst):
    # This function will be tested with up to four categories.
    # if len(lst) > 4:
    #     print('Not more than four Categories')
    #     return
    
    # Takes a list of categories as an argument, return a string that is a bar chart.
    # The chart show the percentage spent in each category passed in to the function

    # Begin the returned string (ret_str) with title 
    #ret_str = 'Percentage spent by category \n'
    # 
    print('Percentage spent by category')

    # Calc each wdrs sum and store in a dict. (then sum(di.values()), for big_total)
    di = {}
    for cat in lst:
        tot_w_cat = 0
        for wd in cat.ledger:
            if wd['amount'] < 0:            # only wthdrs are less than 0 
                tot_w_cat += -wd['amount']  # chg sign cause aoriginal is neg.
        di[cat.name] = tot_w_cat            # Add results to di (still not %)
    print(di, '\n', sum(di.values()))
    # Calc the required % and store in the same dict, respective key
    big_tot = sum(di.values())
    for k in di:
        di[k] = di[k] * 100 / big_tot
    print(di, '\n', sum(di.values()))


            
fo = Category('food')
clo = Category('clothing')
aut = Category('Auto')

fo.deposit(1000, 'initial deposit')
fo.withdraw(10.15, 'groceries')
fo.withdraw(15.89, 'restaurant and mode foodnessty')
fo.transfer(50, clo)

clo.withdraw(13.67789, 'Taxes')
clo.transfer(20, aut)

aut.withdraw(16.0678723, 'Adueded takes and extra charges for late pay')
aut.transfer(2.5, clo)

create_spend_chart([fo, clo, aut])