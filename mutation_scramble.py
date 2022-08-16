from two_randint import *
import random


def scramble_mutation(s):
    a, b = two_randint(len(s))
    print(a, b)
    for i in range(6):
        a2 = random.randint(a, b)
        b2 = random.randint(a, b)
        c = s[a2]
        s[a2] = s[b2]
        s[b2] = c
    return s
