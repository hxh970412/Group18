from two_randint import *


def swap_mutation(s):
    a, b = two_randint(len(s))
    print(a, b)
    s[a], s[b] = s[b], s[a]
    return s
