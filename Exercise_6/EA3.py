from ast import main
import sys
from mutation_swap import swap_mutation
sys.path.append("Exercise_2")
sys.path.append("Exercise_3")
sys.path.append("Exercise_4")
sys.path.append("Exercise_5")

from read_tsp import *
from IndividualAndPopulation import *
from PMX_Crossover import *
from mutation_scramble import *
from fitness_proportional import *
from elitism import *

class EA_3:
    '''This class will use fitness selection, cycle crossover and mutation insert'''
    def __init__(self) -> None:
        pass
    def main(self): # the main function to run each tsp, population size and generations
        tspList = ['EIL51.tsp', 'EIL76.tsp', 'EIL101.tsp', 'ST70.tsp', 'KROA100.tsp', 'KROC100.tsp', 'LIN105.tsp', 'PCB442.tsp', 'PR2392.tsp', 'USA13509.tsp']
        popsizeList = [10, 20, 50, 100]
        generations = [5000, 10000, 20000]
        Note=open('EA3.txt',mode='w')
        for item in tspList:
            for size in popsizeList:
                for generation in generations:
                    result = EA_3.runEA("Exercise_6\dataset\\" + item, size, generation)
                    Note.write(result)
        Note.close()

    def runEA(self,tspName, popSize, generations): # The EA running function
        data = read_tsp.get_data(tspName)
        matrix = IndividualAndPopulation.makeTheMatrix(data)
        pops = IndividualAndPopulation.makePopulation(data, popSize)
        fitness = []
        for item in pops:
            fitness.append(IndividualAndPopulation.calIndDist(item, matrix))

        best_fits = max(fitness)
        best_pop = pops[fitness.index(best_fits)]

        best_fit_list = [best_fit]
        generation = 0
        while generation < generations:
            fit_selection = fitness_proportional(pops, fitness)
            # selection using fitness
            child_pop1, child_fits1 = fit_selection.fitness_proportional()
            child_pop2, child_fits2 = fit_selection.fitness_proportional()
            child = []
            # cycle crossover
            for i in range(popSize):
                child.append(pmx_crossover(child_pop1[i], child_pop2[i]))
            # mutation
            child = swap_mutation(child)
            #calculate child distance and fits
            child_distance = []
            child_fits = []
            for item in child:
                dis = IndividualAndPopulation.calIndDist(item, matrix)
                child_distance.append(dis)
                child_fits.append(1 / dis)
            #elitism
            for i in range(popSize):
                elitism_select = elitism(pops[i], fitness[i], child[i], child_fits[i], len(pops[i]) / 10)
                pops[i], fitness[i] = elitism_select.elitism()

            if best_fit > min(fitness):
                best_fit = min(fitness)
                best_pop = pops[fitness.index(best_fit)]
        
            best_fit_list.append(best_fit)
        
            print('The %d times is the best one: %.1f' % (generation, best_fit))
            generation+=1

        #The best travel path
        print(best_pop)
        return best_pop
        
main()
        



