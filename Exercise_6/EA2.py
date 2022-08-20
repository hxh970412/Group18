from functionset.read_tsp import *
from functionset.IndividualAndPopulation import *
from functionset.PMX_Crossover import *
from functionset.mutation_inversion import *
from functionset.fitness_proportional import *
from functionset.elitism import *


class EA_2:
    '''This class will use fitness selection, cycle crossover and mutation insert'''
    def main(): # the main function to run each tsp, population size and generations
        tspList = ['EIL51.tsp', 'EIL76.tsp', 'EIL101.tsp', 'ST70.tsp', 'KROA100.tsp', 'KROC100.tsp', 'LIN105.tsp', 'PCB442.tsp', 'PR2392.tsp', 'USA13509.tsp']
        popsizeList = [10, 20, 50, 100]
        generations = [5000, 10000, 20000]
        Note=open('EA2.txt', mode='w')
        Note.write("start the EA2 \n")
        for item in tspList:
            for size in popsizeList:
                for generation in generations:
                    Note.write(f"The result is generation: {generation} of popsize: {size} of {item}")
                    result_pop, result_fit = EA_2.runEA(f"dataset\{item}", size, generation)
                    Note.write(",".join(str(x) for x in result_pop) + '\n' + "The best distance is: " + str(result_fit) + '\n')
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
            child1 = [None]*popSize
            child2 = [None]*popSize
            child_fit1 = [None]*popSize
            child_fit2 = [None]*popSize
            for i in range(popSize):
                fit_selection = fitness_proportional(pops, fitness)
                # selection using fitness
                child1[i], child_fit1[i] = fit_selection.fitness_proportional()
                child2[i], child_fit2[i] = fit_selection.fitness_proportional()
            child = [None] * popSize

            # cycle crossover
            for i in range(popSize):
                child[i] = pmx_crossover(child1[i], child2[i])

                # mutation
                child[i] = inversion_mutation(child[i])
            #calculate child distance and fits
            child_fits = []
            for item in child:
                dis = IndividualAndPopulation.calIndDist(item, matrix)
                child_fits.append(dis)
            #elitism
            elitism_select = elitism(pops, fitness, child, child_fits, len(pops)//5)
            pops, fitness = elitism_select.elitism()

            if best_fit > min(fitness):
                best_fit = min(fitness)
                best_pop = pops[fitness.index(best_fit)]
        
            best_fit_list.append(best_fit)
        
            print('The %d times is the best one: %.1f' % (generation, best_fit))
            generation+=1

        #becuase during EA the id of city is start 0 so make it to 1
        for i in range(len(best_pop)):
            best_pop[i] += 1
        #The best travel path
        print(best_pop)
        return best_pop, best_fit
        
EA_2.main()
        



