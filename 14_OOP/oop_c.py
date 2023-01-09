''' Objects Lidecycle'''

class PartyAnimal:
    class_var = 1122
    name = 'class_var name'

    def __init__(self, z):      # constructor
        self.x = 0
        self.name = z
        print('Constructor build', self.name, ' - x:', self.x)

    def party(self):
        self.x += 1
        print('So far:', self.x)    

    def __del__(self):          # destructor
        # r = input('Are you sure? ')
        print('Destructor DELETE', self.name, ' - x:', self.x)

print()
an = PartyAnimal('Tiger')
an.party()
PartyAnimal.party(an)
an = 42
print("Now 'an':", an, type(an))
print()

az = PartyAnimal('Goose')
ax = PartyAnimal('Dog')
ax.party()
print(ax.name)
del(az)
print()

#a = input()

# when program finish ALL objs. are DELETED!?
