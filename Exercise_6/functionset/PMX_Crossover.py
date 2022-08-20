from functionset.two_randint import *
import numpy as np
import copy


def pmx_crossover(mum, dad):
    alice = copy.deepcopy(mum)
    bob = copy.deepcopy(dad)
    alice = np.array(alice)
    bob = np.array(bob)
    r_a_b = None
    size = len(mum)
    a, b = two_randint(size)
    # print(a, b)
    if r_a_b is None:
        r_a_b = range(a, b)
    r_left = np.delete(range(size), r_a_b)
    #print(r_left)
    left_1, left_2 = alice[r_left], bob[r_left]
    middle_1, middle_2 = alice[r_a_b], bob[r_a_b]
    alice[r_a_b], bob[r_a_b] = middle_2, middle_1
    mapping = [[], []]
    for i, j in zip(middle_1, middle_2):
        if j in middle_1 and i not in middle_2:
            index = np.argwhere(middle_1 == j)[0, 0]
            value = middle_2[index]
            while True:
                if value in middle_1:
                    index = np.argwhere(middle_1 == value)[0, 0]
                    value = middle_2[index]
                else:
                    break
            mapping[0].append(i)
            mapping[1].append(value)
        elif i in middle_2:
            pass
        else:
            mapping[0].append(i)
            mapping[1].append(j)
    for i, j in zip(mapping[0], mapping[1]):
        if i in left_1:
            left_1[np.argwhere(left_1 == i)[0, 0]] = j
        elif i in left_2:
            left_2[np.argwhere(left_2 == i)[0, 0]] = j
        if j in left_1:
            left_1[np.argwhere(left_1 == j)[0, 0]] = i
        elif j in left_2:
            left_2[np.argwhere(left_2 == j)[0, 0]] = i
    alice[r_left], bob[r_left] = left_1, left_2
    return alice
