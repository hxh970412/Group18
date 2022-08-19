from functionset.two_randint import *
import numpy as np

def insert_mutation(s):
    a, b = two_randint(len(s))
    # print(a, b)
    np.insert(s, a+1, s[b])
    # s = np.delete(s, len(s)-1, 0)
    return s.tolist()

