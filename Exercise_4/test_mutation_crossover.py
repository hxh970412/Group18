from mutation_insert import *
from mutation_swap import *
from mutation_inversion import *
from mutation_scramble import *
from Order_crossover import *
from PMX_Crossover import *
from cycle_crossover import *
import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a1 = insert_mutation(a)
b1 = swap_mutation(b)
c1 = inversion_mutation(c)
d1 = scramble_mutation(d)

print('initial input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print('result for insert :', a1)
print('result for swap :', b1)
print('result for reverse :', c1)
print('result for scramble :', d1)

mum = np.array([8, 4, 7, 3, 6, 2, 5, 1, 9, 0])
dad = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
##mum = [0, 1, 2, 3, 4, 5, 6]
##dad = [0, 1, 2, 3, 4, 5, 6]
print('initial parent :', mum, dad)
m, n = order_crossover(mum, dad)
print('result for order :', m, n)
m2, n2 = pmx_crossover(mum, dad)
print('result for PMX :', m2, n2)
m3, n3 = cycle_crossover(mum, dad)
print('result for cycle :', m3, n3)

