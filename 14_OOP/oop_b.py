''' Objects: A Sample Class - dir() & type()'''

class PartyAnimal:
    c_x = 0     # class variable: idem for all class objects (instances)
    class_var2 = 1122
    #class_var2 = sum(list(map(lambda x: ord(x), 'PartyAnimal')))

    def __init__(self, inst):
        self.i_x = 0
        self.y = 'a'
        self.inst = inst
        PartyAnimal.c_x += 1   # count objs instanciated

    def party(self):
        self.i_x += 1
        self.y = chr(ord(self.y) + 1)
        print('So far;   c_x: {},  i_x: {},  y: {},  ({})'.format(
            PartyAnimal.c_x,self.i_x, self.y, self.inst))

    def get_state(self):
        print()
        print(f"Obj. '{self.inst}', own vars: {self.__dict__}")
        # parent_class = eval(self.inst).__class__
        # print('Class origin {} own vars; c_x: {}, class_var2: {}'.format(
        #     parent_class.__name__, parent_class.c_x, parent_class.class_var2))
        print("Class origin '{}', own vars; c_x: {}, class_var2: {}".format(
            PartyAnimal.__name__, PartyAnimal.c_x, PartyAnimal.class_var2))
        

one = PartyAnimal('one')
one.get_state()
one.party()
one.party()
PartyAnimal.party(one)
PartyAnimal.get_state(one)

two = PartyAnimal('two')
two.get_state()
two.party()
PartyAnimal.party(two)
two.get_state()

three = PartyAnimal('three')
three.get_state()
three.party()
three.get_state()

print()