''' Scientific Computing with Python - Probability Calculator'''

# prob_calculator_v0.py
import random
import copy

def mk_balls_list(di):
    ''' Aux funct. that convert input dict to ret_lst: a list of
    strings containing di_value numbers of str-items (di-key) '''   
    ret_lst = []
    for k, v in di.items():
        for i in range(v): ret_lst.append(k)
    return ret_lst


class Hat():
    ''' This class  take a variable number of arguments that specify the number of balls of each
    color that are in the hat. A hat will always be created with at least one ball. The arguments
    passed into the hat object upon creation should be converted to a contents instance variable.
    contents should be a list of strings containing one item for each ball in the hat'''

    def __init__(self, **kargs):
        self.contents = mk_balls_list(kargs)

    # .draw() accepts an argument indicating the number of balls to draw from the hat.
    # similar to an urn experiment without replacement.
    def draw(self, num_balls):
        try: 
            drwlst = random.sample(self.contents, num_balls)
        except ValueError:
            drwlst = self.contents.copy()       # simple asigment (wo/copy) mk an alias
        # Now remove de drwlst elements (balls) from self.contents
        for ball in drwlst:
            self.contents.remove(ball)
        return drwlst


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''  Return the probability of getting exp_balls drawning n_b_d from balls
    in hat obj, making a total of num_e.
    hat: Hat obj., exp_balls: dict, num_b_d: int, num_e: int'''

    orighat = copy.deepcopy(hat)

    # expexted_balls (dict) are fixed for all experiments
    exp_balls_lst = mk_balls_list(expected_balls)   # list  conversion of exp_balls dict
    
    len_ebl = len(exp_balls_lst)    # to use to known if all the exp_balls was matched
    succ_exp_cnt = 0                # initialize succesful experiment counter

    for i in range(num_experiments):                # for e/experiment (mk n experimentes)
        hat = copy.deepcopy(orighat)                               # e/test return the hat to its orig value
        drwn_balls_lst = hat.draw(num_balls_drawn)  # obtain the list of drawn n_balls from hat
        matchs = 0                                  # initialize balls matchs counter
        for exp_ball in exp_balls_lst:              # for e/ball in e_b_l
            # find if the exp_ball is in de drawn balls, if -> add matchs & remove from drwn_b_list
            if exp_ball in drwn_balls_lst:
                matchs += 1         # Add one match cause exp_ball is IN the list of drwn_balls
                # last remove element from drwn_balls_lst cause was already matched
                drwn_balls_lst.remove(exp_ball)
        # if nbr of matchs idem length of exp_balls_lst then IS a succesful experiment 
        if matchs == len_ebl: succ_exp_cnt += 1

    return succ_exp_cnt / num_experiments

## --- main.py ---
# random.seed(95)
# hat = Hat(blue=4, red=2, green=6)
# probability = experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)


## --- main_JM ---
hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)

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

# ## Other try of return list asigment
# print()
# print('hat.contents:', hat.contents)
# s1 = hat.draw(25); print('s1:', s1)
# print('hat.contents:', hat.contents)
# s2 = hat.draw(5); print('s2:', s2)
# print('hat.contents:', hat.contents)
# s3 = hat.draw(-100); print('s3:', s3)
# print('hat.contents:', hat.contents)
# print()

# del s1[0]; print('s1:', s1)
# print('s2:', s2)
# print('hat.contents:', hat.contents)




