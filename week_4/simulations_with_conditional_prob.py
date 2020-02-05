import numpy as np
bag1 = None
bag2 = None
box  = None

bag1, bag2, box

bag1 = {'marbles': np.array(['black', 'white'], dtype='<U5'),
  'probs': np.array([0.4, 0.6])}

bag2 = {'marbles': np.array(['black', 'white'], dtype='<U5'),
  'probs': np.array([0.7, 0.3])}

box = {'bags': np.array([{'marbles': np.array(['black', 'white'], dtype='<U5'), 'probs': np.array([0.4, 0.6])},
         {'marbles': np.array(['black', 'white'], dtype='<U5'), 'probs': np.array([0.7, 0.3])}],
        dtype=object), 'probs': np.array([0.5, 0.5])}



def sample_marble(box):
    # randomly choose a bag
    bag = None
    rint = np.random.randint(100)
    rdec = np.random.random()
    if (rint % 2):
            bag = box['bags'][0]
            if(rdec <= bag['probs'][0]):
                return bag['marbles'][0]
            else:
                return bag['marbles'][1]
    else:
            bag = box['bags'][1]
            if(rdec <= bag['probs'][0]):
                return bag['marbles'][0]
            else:
                return bag['marbles'][1]

def probability_of_color(color, box, num_samples=1000):
    # get a bunch of marbles
    colors = [sample_marble(box) for x in range(num_samples)]
    # compute fraction of marbles of desired color
    freq = colors.count(color) / len(colors)
    return freq
#sample_marble(box)
# 'black' OR 'white'



# Change above code here
import numpy as np
bag1 = None
bag2 = None
box  = None

bag1, bag2, box

bag1 = {'marbles': np.array(['black', 'white', 'gray'], dtype='<U5'),
  'probs': np.array([4/15, 6/15, 5/15])}

bag2 = {'marbles': np.array(['black', 'white', 'gray'], dtype='<U5'),
  'probs': np.array([7/15, 3/15, 5/15])}

box = {'bags': np.array([{'marbles': np.array(['black', 'white', 'gray'], dtype='<U5'),
  'probs': np.array([4/15, 6/15, 5/15])},
                        {'marbles': np.array(['black', 'white', 'gray'], dtype='<U5'),
  'probs': np.array([7/15, 3/15, 5/15])}],
        dtype=object), 'probs': np.array([2/3, 1/3])}

#np.random.choice(box['bags'], p=box['probs'])

def sample_marble(box):
    # randomly choose a bag
    bag = None
    rbag = np.random.random()
    rdec = np.random.random()
    if (rbag <= box['probs'][0]): #bag1
            bag = box['bags'][0]
            if(0 <= rdec <= bag['probs'][0]): #black
                return bag['marbles'][0]
            elif ( bag['probs'][0] <= rdec <= bag['probs'][1] + bag['probs'][0] ): #white
                return bag['marbles'][1]
            else: #gray
                return bag['marbls'][2]
    else: #bag2
            bag = box['bags'][1]
            if(0 <= rdec <= bag['probs'][0]): #black
                return bag['marbles'][0]
            elif ( bag['probs'][0] <= rdec <= bag['probs'][1] + bag['probs'][0] ): #white
                return bag['marbles'][1]
            else: #gray
                return bag['marbls'][2]
