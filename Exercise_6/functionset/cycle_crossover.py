import numpy as np
import copy


def cycle_crossover(mum, dad): # cycle corssover function

    size = len(mum)
    child1 = np.array([-1] * size)
    child2 = np.array([-1] * size)

    p1_copy = copy.deepcopy(mum)
    p2_copy = copy.deepcopy(dad)
    swap = True
    count = 0
    pos = 0

    while True:
        if count > size:
            break
        for i in range(size):
            if child1[i] == -1:
                pos = i
                break

        if swap:
            while True:
                child1[pos] = mum[pos]
                count += 1
                pos = dad.index(mum[pos])
                if p1_copy[pos] == -1:
                    swap = False
                    break

                p1_copy[pos] = -1
        else:
            while True:
                child1[pos] = dad[pos]
                count += 1
                pos = mum.index(dad[pos])
                if p2_copy[pos] == -1:
                    swap = True
                    break
                p2_copy[pos] = -1

        for i in range(size):
            if child1[i] == mum[i]:
                child2[i] = dad[i]
            else:
                child2[i] = mum[i]

        for i in range(size):
            if child1[i] == -1:
                if p1_copy[i] == -1:
                    child1[i] = dad[i]
                else:
                    child1[i] = mum[i]

    return child1
