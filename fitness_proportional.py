import random

class fitness_proportional:

    def __init__(self, fits, pops):
        self.fits = fits
        self.pops = pops


    '''This function is using to select the best offspring by fitness proportional selection'''
    def fitness_proportional(self):
        fits = self.fits
        pops = self.pops
        # sum the fitness
        fits_sum = sum(fits)
        # make a random number between 0 - 1 like pointer on roulette
        t = random.random()
        # start with a random parent 
        i = random.randint(0, len(fits) - 1)


        '''go throught all fitsness untill the t under the proportion of fit in the total 
        that means the pointer reach'''
        while t > fits[i] / fits_sum:
            t = random.random()
            i = (i + 1) % len(fits)
        return fits[i], pops[i]