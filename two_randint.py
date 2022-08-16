import random


def two_randint(size):
    b = a = random.randint(0, size - 1)
    while a == b:
        b = random.randint(0, size - 1)
    if a > b:
        return b, a
    return a, b
