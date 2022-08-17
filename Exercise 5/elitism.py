from array import array
from multiprocessing.dummy import Array
from operator import index


class elitism:
    def __init__(self, parents, parent_fits, offspring, offpsring_fits, elitism_num):
        self.parents = parents
        self.parent_fits = parent_fits
        self.offspring = offspring
        self.offpsring_fits = offpsring_fits
        self.elitism_num = elitism_num

    def elitism(self):
        parents = self.parents
        parent_fits = self.parent_fits
        offspring = self.offspring
        elitism_num = self.elitism_num
        new_offspring = self.offspring
        new_offspring_fits = self.offpsring_fits
        elitism_fitness_list = []
        elitism_list = []

        for index,item in enumerate(sorted(parent_fits)):
            if (index >= len(parent_fits) - elitism_num):
                elitism_fitness_list.append(item)
                new_offspring_fits.append(item)

        for index, item in enumerate(parent_fits):
            if (item in elitism_fitness_list):
                elitism_list.append(sorted(parents)[index])
                new_offspring.append(sorted(parents)[index])

        return new_offspring, new_offspring_fits