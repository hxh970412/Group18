import random

class tournament_selection:

    def __init__(self, pops,fits,tournament_size):
        self.pops = pops
        self.fits = fits
        self.tournament_size =  tournament_size

    ''' This function is using to select the best offspring by tournament selection'''
    def tournament_selection(self):
        pops = self.pops
        fits = self.fits
        tournament_size = self.tournament_size
        popsize = len(pops)
        #set the offspring list
        offspring_pops, offspring_fits = [], []
        #loop untill the offspring size is same as parent size
        while len(offspring_pops) < popsize:
            # Randomly obtain the individual of the tournament 
            tournament_list = random.sample(range(0, popsize), tournament_size)
            # set the fitness of them
            tournament_fits = []
            for index in range(0, popsize):
                if (index in tournament_list):
                    tournament_fits.append(fits[index])
            # find the best one
            fits_max = 0
            for item in tournament_fits:
                if (item > fits_max):
                    fits_max = item

            # add to the offspring
            offspring_pops.append(pops[fits.index(fits_max)])
            offspring_fits.append(fits_max)
        return offspring_pops, offspring_fits