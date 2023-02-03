''' Scientific Computing with Python - Probability Calculator'''

# prob_calculator_v0.py
from random import sample

def mk_balls_list(di):
    ''' Aux funct. that convert input dict to ret_lst: a list of
    strings containing di_value numbers of str-items (di-key) '''   
    ret_lst = []
    for k, v in di.items():
        for i in range(v): ret_lst.append(k)
    return ret_lst


class Hat():
    def __init__(self, **kargs):
        self.contents = mk_balls_list(kargs)

    def draw(self, num_balls):
        try: 
            drwlst = sample(self.contents, num_balls)
        except ValueError:
            drwlst = self.contents
        return drwlst


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''  Return the probability of getting exp_balls drawning n_b_d from balls
    in hat obj, making a total of num_e.
    hat: Hat obj., exp_balls: dict, num_b_d: int, num_e: int'''

    # print()
    # print('hat.contents', hat.contents)

    # expexted_balls (dict) are fixed for all experiments
    exp_balls_lst = mk_balls_list(expected_balls)   # list  conversion of exp_balls dict
    
    len_ebl = len(exp_balls_lst)    # to use to known if all the exp_balls was matched
    # print('exp_balls_lst:', exp_balls_lst, ' - len_ebl:', len_ebl)
    succ_exp_cnt = 0                # initialize succesful experiment counter
    # print()

    for i in range(num_experiments):                # for e/experiment (mk n experimentes)
        drwn_balls_lst = hat.draw(num_balls_drawn)  # obtain the list of drawn n_balls from hat
        # print('drwn_balls_lst:', drwn_balls_lst, ' - exp:', i)
        matchs = 0                  # initialize balls matchs counter
        for exp_ball in exp_balls_lst:    # for e/ball in e_b_l
            # find if the exp_ball is in de drawn balls, if -> add matchs & remove from drwn_b_list
            if exp_ball in drwn_balls_lst:
                matchs += 1     # Add one match
                # last remove element from drwn_balls_lst cause was already matched
                drwn_balls_lst.remove(exp_ball)
        # if nbr of matchs idem length of exp_balls_lst then IS a succesful experiment 
        if matchs == len_ebl: succ_exp_cnt += 1

    return succ_exp_cnt / num_experiments


## --- main ---
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

for i in range(7):
    print('Probability:', experiment(hat, {"red":2,"green":1}, 5, 200000))

# ## To test Hat.draw() method
# print()
# print('hat.contents:', hat.contents, '\n')
# for i in range(3):
#     print(hat.draw(5))
#     print('hat.contents:', hat.contents, '\n')
# print(hat.draw(15))
# print(hat.draw(-1))
# print(hat.draw(100))
# print(hat.draw(-100))
