''' Scientific Computing w/Python'''

# budget_v0.py                  # presupuesto

class Category:
    def __init__ (self, category):
        self.name = category
        self.ledger = []        # ledger -> libro mayor
        self.__blnc = 0         # calc. balance on the fly       

    # Register a deposit in ledger[]
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    # Register a withdraw in ledger[] (chge amount to neg before)
    def withdraw(self, amount, description=''):
        if self.check_founds(amount):
            self.ledger.append({'amount':  -amount,
                     'description': description})
            return True
        else: return False

    def get_balance(self):
        self.__blnc = 0
        for el in self.ledger:
            self.__blnc += el['amount']
        return self.__blnc

    def transfer(self, amount, obj):
        pass

    def check_founds(self, amount):
        if amount > self.get_balance(): 
            self.__blnc = 0
            return False
        else:
            self.__blnc = 0
            return True

    def __str__(self):
        res = self.name.center(30, '*') + '\n'
        for el in self.ledger:
           res += ('{:<23} {:>7}'.format(el['description'], el['amount']) +
                    '\n') 
        res += 'Total: ' + str(self.get_balance())
        return res

def create_spend_chart(lst):
    pass
            

fo = Category('food')
#print(fo)
fo.deposit(1000, 'initial deposit')
#fo.withdraw(10.15, 'groceries')
fo.deposit(300, 'rent transf')
fo.withdraw(10.15, 'groceries')
#print(fo.__dict__)
# fo.deposit(.5, 'tax recover')
print()
print(fo)
print()
print(fo.get_balance())
print(fo.get_balance())
print()
print(fo.withdraw(5000))
print(fo.get_balance())
print(fo.__dict__)


