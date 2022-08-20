import random

class tournament_selection:


    ''' This function is using to select the best offspring by tournament selection'''
    def tournament_selection(pops, fits, tournament_size, popsize):
        #set the offspring list
        offspring_pops, offspring_fits = [], []
        #loop untill the offspring size is same as parent size
        # Randomly obtain the individual of the tournament 
        tournament_list = random.sample(range(0, popsize), tournament_size)
        # set the fitness of them
        tournament_fits = []
        for index in range(0, popsize):
            if (index in tournament_list):
                tournament_fits.append(fits[index])
        # find the best one
        fits_min = tournament_fits[0]
        for item in tournament_fits:
            if (item < fits_min):
                fits_min = item   

        return pops[fits.index(fits_min)], fits_min