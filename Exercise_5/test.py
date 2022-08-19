from fitness_proportional import fitness_proportional
from tournament_selection import tournament_selection
from elitism import elitism

test_pops = [45, 34, 54, 23]
test_fits = [0.3, 0.2, 0.4, 0.1]
test_tournament_size = 3
elitism_num = 2

right_answer = []

# print("tournament_selection: ")
# tournament_s = tournament_selection()
# for i in range(0, 10):

#     offspring_pops, offspring_fits = tournament_s.tournament_selection(test_pops, test_fits, test_tournament_size)
#     print(f"The {i} time: ", offspring_pops, offspring_fits)
#     eli = elitism(test_pops, test_fits, offspring_pops, offspring_fits, elitism_num)
#     print(f"The {i} time elitism: ", eli.elitism())
#     # if (out == right_answer):
#     #     print("out put is right")

# print("\n")
# print("fitness_proportional: ")
# fitness_selection = fitness_proportional(test_fits, test_pops)
# for i in range(0, 10):
#     print(fitness_selection.fitness_proportional())

off = [11, 10, 13, 12]
off_fits = [0.2, 0.1, 0.4, 0.3]
eli = elitism(test_pops, test_fits, off, off_fits, elitism_num)
print(eli.elitism())
