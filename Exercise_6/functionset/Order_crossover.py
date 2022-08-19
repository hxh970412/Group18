from functionset.two_randint import *


def order_crossover(mum, dad):
    size = len(mum)

    # Choose random start/end position for crossover
    a, b = two_randint(size)
    child1, child2 = [-1] * size, [-1] * size

    # Replicate mum's sequence for alice, dad's sequence for bob
    alice_inherited = []
    bob_inherited = []
    for i in range(a, b + 1):
        child1[i] = mum[i]
        child2[i] = dad[i]
        alice_inherited.append(mum[i])
        bob_inherited.append(dad[i])

    # print(alice, bob)
    # Fill the remaining position with the other parents' entries
    current_dad_position, current_mum_position = 0, 0

    fixed_pos = list(range(a, b + 1))
    i = 0
    while i < size:
        if i in fixed_pos:
            i += 1
            continue

        test_alice = child1[i]
        if test_alice == -1:  # to be filled
            dad_trait = dad[current_dad_position]
            while dad_trait in alice_inherited:
                current_dad_position += 1
                dad_trait = dad[current_dad_position]
            child1[i] = dad_trait
            alice_inherited.append(dad_trait)

        test_bob = child2[i]
        if test_bob == -1:  # to be filled
            mum_trait = mum[current_mum_position]
            while mum_trait in bob_inherited:
                current_mum_position += 1
                mum_trait = mum[current_mum_position]
            child2[i] = mum_trait
            bob_inherited.append(mum_trait)

        i += 1

    return child1
