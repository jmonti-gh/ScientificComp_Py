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

    def draw(self, num_balls):
        drwlst = []
        if num_balls > len(self.contents):
            return self.contents
        for i in range(num_balls):
            ix = randint(0, len(self.contents) - 1)
            drwlst.append(self.contents.pop(ix))
        return drwlst


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''  Return the probability of getting exp_balls drawning n_b_d from balls
    in hat obj, making a total of num_e.
    hat: Hat obj., exp_balls: dict, num_b_d: int, num_e: int'''

    drwn_balls_lst = hat.draw(num_balls_drawn)      # list of drawn n_balls from hat
    #print('drwn_balls_lst:',  drwn_balls_lst)
    exp_balls_lst = mk_balls_list(expected_balls)   # list  conversion of exp_balls dict
    # print('exp_balls_lst', exp_balls_lst)
    # print()
    len_ebl = len(exp_balls_lst)    # to use to known if all the exp_balls was matched
    
    #print(expected_balls, exp_balls_lst)
    succ_exp_cnt = 0      # succesful experiment counter
    for i in range(num_experiments):
    # for all the experiments - first - try with only ONE experiment f
        matchs = 0
        for el in exp_balls_lst:        # for e/ball in e_b_l
            # print(exp_balls_lst, el)
            # print('drwn_balls_lst:',  drwn_balls_lst)
            # look for the expected element in the list of drawn elements
            if el in drwn_balls_lst:
                #print('MATCH!')
                matchs += 1     # Add one match
                # last remove element from drwn_balls_lst cause was already matched
                drwn_balls_lst.remove(el)
            #else: print(' ------ no match!')
        #print(matchs)    
        if matchs == len_ebl:
            print('----- IUNO -------')
            succ_exp_cnt += 1
    print(succ_exp_cnt)

    return succ_exp_cnt/num_experiments



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

# print(hat.contents)
# exp_balls_lst = mk_balls_list({"red":2,"green":1})
# drawn_balls = hat.draw(5) 
# exp_balls_lst.sort()
# print(exp_balls_lst)
# drawn_balls.sort()
# print(drawn_balls)
# exp_balls_lst.sort()
# print(exp_balls_lst in drawn_balls)

# print()
# hat40 = Hat(red=2, orange=3, black=1, blue=0, pink=2, striped=4)
# print(hat40.contents)
# print(hat40.draw(25))
# print(hat40.draw(4))
# print(hat40.contents)

# print()
# h0 = Hat(red=2, blue=1)
# print(h0.contents)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat3.contents)
# print()

