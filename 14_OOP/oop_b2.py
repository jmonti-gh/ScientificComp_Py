''' Objects: A Sample Class - Playing with dir() & type()'''

class PartyAnimal:
    class_var2 = 1122

    def __init__(self):
        self.i_x = 0

    def party(self):
        self.i_x += 1
        print('So far:', self.i_x)        

print()
an = PartyAnimal()
an.party()
PartyAnimal.party(an)
print()

# # dir() & type() to inspect variables, types, and objects. Both tell us
# # something about the object. dir() lists capabilities. 
# # type() tell us what kind of object is x (by eg.)
# x = []
# print(x, type(x), '\n', dir(x), '\n')
# y = 'Hi Py'
# print(y, type(y), '\n', dir(y), '\n')
# # for an object above instaciated
# print(an, type(an), '\n', dir(an), '\n')

t = (x, y, az) = (list(), str(3.1416), PartyAnimal())
print(t, '\n')
for obj in t:
    print(obj, type(obj), '\n', dir(obj), '\n')

# ta = (l, s, az, t, d, et) = (list(), str(3.1416), 
# PartyAnimal(), tuple(), dict(), set())
# print(ta, '\n')
# for obj in ta:
#     print(obj, type(obj), '\n', dir(obj), '\n')

# print(l, type(l), '\n', dir(l), '\n')
# print(an, type(an), '\n', dir(an), '\n')
