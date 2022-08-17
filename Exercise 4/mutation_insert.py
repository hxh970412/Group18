from two_randint import *


def insert_mutation(s):
    a, b = two_randint(len(s))
    print(a, b)
    s.insert(a+1, s[b])
    s.pop(b+1)
    return s

