from array import array
from multiprocessing.dummy import Array
from operator import index


class elitism:
    def __init__(self, parents:list, parent_fits: list, offspring: list, offpsring_fits: list, elitism_num):
        self.parents = parents
        self.parent_fits = parent_fits
        self.offspring = offspring
        self.offpsring_fits = offpsring_fits
        self.elitism_num = elitism_num

    def elitism(self): # the elitism selection
        parents = self.parents
        parent_fits = self.parent_fits
        offspring = self.offspring
        elitism_num = self.elitism_num
        new_offspring = self.offspring
        new_offspring_fits = self.offpsring_fits
        #print (self.parent_fits)
        parent_fits_copy = sorted(self.parent_fits)
        
        offspring_fits = sorted(self.offpsring_fits)
        
        for i in range (elitism_num):
            new_offspring[new_offspring_fits.index(offspring_fits[len(offspring_fits) - 1 - i])] = parents[parent_fits.index(parent_fits_copy[i])]
            new_offspring_fits[new_offspring_fits.index(offspring_fits[len(offspring_fits) - 1 - i])] = parent_fits_copy[i]

        return new_offspring, new_offspring_fits