import sys
sys.path.append("Exercise_2")
sys.path.append("Exercise_3")
sys.path.append("Exercise_4")
sys.path.append("Exercise_5")

from read_tsp import *
from IndividualAndPopulation import *
from cycle_crossover import *
from mutation_insert import *
from fitness_proportional import *

class EA_1:
    def __init__(self) -> None:
        pass
    def main(self):
        tspList = ['EIL51.tsp', 'EIL76.tsp', 'EIL101.tsp', 'ST70.tsp', 'KROA100.tsp', 'KROC100.tsp', 'LIN105.tsp', 'PCB442.tsp', 'PR2392.tsp', 'USA13509.tsp']
        popsizeList = [10, 20, 50, 100]
        generations = [5000, 10000, 20000]
        for item in tspList:
            for size in popsizeList:
                for generation in generations:
                    EA_1.runEA("Exercise_6\dataset\\" + item, size, generation)

    def runEA(self,tspName, popSize, generations):
        data = read_tsp.get_data(tspName)
        matrix = IndividualAndPopulation.makeTheMatrix(data)
        pops = IndividualAndPopulation.makePopulation(data, popSize)
        distance = []
        for item in pops:
            distance.append(IndividualAndPopulation.calIndDist(item, matrix))
        fitness = []
        for item in distance:
            fitness.append(1 / item)

        i = 0
        while i < generations:
            
            i+=1

        



