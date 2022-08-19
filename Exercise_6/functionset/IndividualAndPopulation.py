import math
import pandas as pd
import random

class IndividualAndPopulation:
    def makeTheMatrix(city_list): # calculate the distance between each point and make a matrix for easy check
        dis_matrix = pd.DataFrame(data=None,columns=range(len(city_list)),index=range(len(city_list)))
        for i in range(len(city_list)):
            xi,yi = city_list[i][0],city_list[i][1]
            for j in range(len(city_list)):
                xj,yj = city_list[j][0],city_list[j][1]
                dis_matrix.iloc[i,j] = round(math.sqrt((xi-xj)**2+(yi-yj)**2),2)

        return dis_matrix

    def calIndDist(individual, dis_matrix): # calculate each parent's distance
        dis_sum = 0
        for i in range(len(individual)):
            if i < len(individual)-1:
                dis_sum += dis_matrix.loc[individual[i],individual[i+1]] 
            else:
                dis_sum += dis_matrix.loc[individual[i],individual[0]]
        return round(dis_sum, 3)

    def makePopulation(city_list, popSize): # make the parents
        pops = [random.sample([i for i in list(range(len(city_list)))],len(city_list)) for j in range(popSize)]

        return pops


