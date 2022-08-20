from two_randint import *
import numpy as np


def insert_mutation(s):

    a, b = two_randint(len(s))
    print(a, b)
    s_l = s.tolist()
    s_l.insert(a+1, s[b])
    s = np.asarray(s_l)
    #np.insert(s, a+1, s[b])
    s = np.delete(s, b+1, )
    return s.tolist()


