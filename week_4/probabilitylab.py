roll_dice = {1,2,3,4,5,6}

event = {5,6}

prob_5_6 = len(event) / len (roll_dice)
prob_5_6  # 0.3333333333333333

import numpy as np
np.random.randint(1,7) # you will get a random value between 1 and 6. See how it changes when you rerun

np.random.seed(12345) # to ensure reproducibility of results

dice_10 = np.random.randint(1,7,size= 10)
dice_1k = np.random.randint(1,7,size= 1000)
dice_1m = np.random.randint(1,7,size=1000000)
dice_100m = np.random.randint(1,7,size=100000000)

event_10 = [x in event for x in dice_10].count(True)
event_1k = [x in event for x in dice_1k].count(True)
event_1m = [x in event for x in dice_1m].count(True)
event_100m = [x in event for x in dice_100m].count(True)


prob_10 = event_10 / 10
prob_1k = event_1k / 1000
prob_1m = event_1m / 1000000
prob_100m = event_100m / 100000000
prob_10, prob_1k, prob_1m, prob_100m  # 0.5 0.331 0.333657 0.33329752

P_afr = 0.161
P_ant = 0.000
P_as = 0.598
P_eur = 0.10
P_na = 0.079
P_aus = 0.005
P_sa = 0.057

continents = np.array([P_afr, P_ant, P_as, P_eur, P_na, P_aus, P_sa])
print(continents)


def check_axioms(sample_space):
    for x in sample_space :
        if (x > 1):
            return 'not quite!'
        elif (x < 0):
            return 'not quite!'
    if (sum(sample_space) > 1) :
        return "not quite!"
    else :
        return """We're good!"""



check_axioms(continents)


test_1 = np.array([0.05, 0.2, 0.3, 1.01])
test_2 = np.array([0.05, 0.5, 0.6, -0.15])
test_3 = np.array([0.043,0.05,.02,0.3,0.2])


#check_axioms(test_1)
#check_axioms(test_2)
check_axioms(test_3)

import numpy as np
sample_dice = np.array([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
              (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
              (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
              (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
              (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
              (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)])

sample_dice.shape # should be equal to (36,2)
