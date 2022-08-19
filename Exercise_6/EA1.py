from functionset.read_tsp import *
from functionset.IndividualAndPopulation import *
from functionset.cycle_crossover import *
from functionset.mutation_insert import *
from functionset.fitness_proportional import *
from functionset.elitism import *

class EA_1:
    '''This class will use fitness selection, cycle crossover and mutation insert'''
    def main(): # the main function to run each tsp, population size and generations
        tspList = ['EIL51.tsp', 'EIL76.tsp', 'EIL101.tsp', 'ST70.tsp', 'KROA100.tsp', 'KROC100.tsp', 'LIN105.tsp', 'PCB442.tsp', 'PR2392.tsp', 'USA13509.tsp']
        popsizeList = [10, 20, 50, 100]
        generations = [5000, 10000, 200000]
        Note=open('EA1.txt',mode='w')
        for item in tspList:
            for size in popsizeList:
                for generation in generations:
                    result = EA_1.runEA(f"dataset\{item}", size, generation)
                    Note.write(result)
        Note.close()

    def runEA(tspName, popSize, generations): # The EA running function
        data = read_tsp.get_data(tspName)
        matrix = IndividualAndPopulation.makeTheMatrix(data)
        pops = IndividualAndPopulation.makePopulation(data, popSize)
        fitness = []
        for item in pops:
            fitness.append(IndividualAndPopulation.calIndDist(item, matrix))

        best_fit = max(fitness)
        best_pop = pops[fitness.index(best_fit)]

        best_fit_list = [best_fit]
        generation = 0
        while generation < generations:
            fit_selection = fitness_proportional(pops, fitness)
            # selection using fitness
            child_pop1, child_fits1 = fit_selection.fitness_proportional()
            child_pop2, child_fits2 = fit_selection.fitness_proportional()
            child = [None] * popSize

            # cycle crossover
            for i in range(popSize):
                child[i] = cycle_crossover(child_pop1, child_pop2)

                # mutation
                child[i] = insert_mutation(child[i])
                print (child[i])
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
        
EA_1.main()
        



