from mutation_insert import *
from mutation_swap import *
from mutation_inversion import *
from mutation_scramble import *
from Order_crossover import *
from PMX_Crossover import *
from cycle_crossover import *
import numpy as np

a = [0, 1, 2, 3, 4, 5, 6]
b = [0, 1, 2, 3, 4, 5, 6]
c = [0, 1, 2, 3, 4, 5, 6]
d = [0, 1, 2, 3, 4, 5, 6]

insert_mutation(a)
swap_mutation(b)
inversion_mutation(c)
scramble_mutation(d)
print('initial input: [0, 1, 2, 3, 4, 5, 6]')
print('result for insert :', a)
print('result for swap :', b)
print('result for reverse :', c)
print('result for scramble :', d)

mum = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
dad = np.array([5, 4, 6, 9, 2, 1, 7, 8, 3])
##mum = [0, 1, 2, 3, 4, 5, 6]
##dad = [0, 1, 2, 3, 4, 5, 6]
print('initial parent :', mum, dad)
m, n = order_crossover(mum, dad)
print('result for order :', m, n)
m2, n2 = pmx_crossover(mum, dad)
print('result for PMX :', m2, n2)
m3, n3 = cycle_crossover(mum, dad)
print('result for cycle :', m3, n3)

