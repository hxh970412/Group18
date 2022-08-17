import numpy as np


def cycle_crossover(mum, dad):

    size = len(mum)
    alice = np.array([-1] * size)
    bob = np.array([-1] * size)

    p1_copy = mum.tolist()
    p2_copy = dad.tolist()
    swap = True
    count = 0
    pos = 0

    while True:
        if count > size:
            break
        for i in range(size):
            if alice[i] == -1:
                pos = i
                break

        if swap:
            while True:
                alice[pos] = mum[pos]
                count += 1
                pos = dad.tolist().index(mum[pos])
                if p1_copy[pos] == -1:
                    swap = False
                    break
                p1_copy[pos] = -1
        else:
            while True:
                alice[pos] = dad[pos]
                count += 1
                pos = mum.tolist().index(dad[pos])
                if p2_copy[pos] == -1:
                    swap = True
                    break
                p2_copy[pos] = -1

        for i in range(size):
            if alice[i] == mum[i]:
                bob[i] = dad[i]
            else:
                bob[i] = mum[i]

        for i in range(size):
            if alice[i] == -1:
                if p1_copy[i] == -1:
                    alice[i] = dad[i]
                else:
                    alice[i] = mum[i]

    return alice, bob
