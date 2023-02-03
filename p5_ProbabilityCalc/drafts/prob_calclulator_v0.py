''' Scientific Computing with Python - Probability Calculator'''

# prob_calculator_v0.py
from random import randint

def mk_balls_list(di):
    ''' Aux funct. that convert input di to ret_lst: a list of
    strings containing di_value num of str-items (di-key) '''      
    ret_lst = []
    for k, v in di.items():
        for i in range(v): ret_lst.append(k)
    return ret_lst


class Hat():
    def __init__(self, **kargs):
        self.contents = mk_balls_list(kargs)
        # for k, v in kargs.items():
        #     self.contents = [k for i in range(v)]
        # #     for i in range(v):
        # #         self.contents.append(k)
        # #self.contents = [k for el in range(v) for k, v in kargs.items()]

    def draw(self, balls):
        drwlst = []
        if balls > len(self.contents):
            return self.contents
        for i in range(balls):
            ix = randint(0, len(self.contents) - 1)
            drwlst.append(self.contents.pop(ix))
        return drwlst


def experiment(hat, expected_balls, num_balls_drwan, num_experiments):
    '''  Return the probability of getting exp_balls drawning n_b_d from balls
    in hat obj, making a total of num_e.
    hat: Hat obj., exp_balls: dict, num_b_d: int, num_e: int'''



    m = 0   # nbr of times you get the exp_balls
    for exp in num_experiments:
        pass
        #if sorted(hat.draw) == sorted(e) 



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

