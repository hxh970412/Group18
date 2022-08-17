from two_randint import *


def inversion_mutation(s):
    a, b = two_randint(len(s))
    print(a, b)
    s[a:b+1] = reversed(s[a:b+1])
    return s
