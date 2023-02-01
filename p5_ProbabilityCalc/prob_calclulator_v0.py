''' Scientific Computing with Python - Probability Calculator'''

# prob_calculator_v0.py
from random import randint

class Hat():
    def __init__(self, **kargs):
        self.contents = []
        for k, v in kargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, balls):
        drwlst = []
        if balls > len(self.contents):
            return self.contents
        for i in range(balls):
            ix = randint(0, len(self.contents) - 1)
            drwlst.append(self.contents.pop(ix))
        return drwlst

print()
hat40 = Hat(red=2, orange=3, black=1, blue=0, pink=2, striped=4)
print(hat40.contents)
print(hat40.draw(25))
print(hat40.draw(4))
print(hat40.contents)

# print()
# h0 = Hat(red=2, blue=1)
# print(h0.contents)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat3.contents)
# print()

