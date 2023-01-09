''' Objects: Inheritance'''

class PartyAnimal:
    c_x = 0     # class variable: idem for all instanes

    def __init__(self, nm):
        self.i_x = 0
        self.name = nm
        PartyAnimal.c_x += 1   # count objs instanciated

    def party(self):
        self.i_x += 1
        print(self.name, 'party count', self.i_x)

    def get_state(self):
        print()
        print(self.name, 'own vars:',  self.__dict__)
        print('PartyAnimal objects count', PartyAnimal.c_x)
        
class FootballFan(PartyAnimal):
    f_x = 0

    def __init__ (self, nm):
        self.points = 0
        FootballFan.f_x += 1   # count FootballFan objs
        super().__init__(nm)   # call superclass construct

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, 'points', self.points)

    def get_state(self):
        PartyAnimal.get_state(self)
        print('FootballFun objects count', FootballFan.f_x)

class SimpleFan(FootballFan):
    def get_state(self):
        FootballFan.get_state(self)
        print('SimpleFan objects count:  -- NOT Registerd ! --')

print()
s = PartyAnimal('Sal')
s.party()
s.get_state()

print()
j = FootballFan('Jim')
j.party()
j.touchdown()
j.get_state()

print()
m = SimpleFan('Mon')
m.party()
m.touchdown()
m.get_state()