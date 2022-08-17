from math import dist
from turtle import distance


class cal_distance:

    def cal_distance(pop, distanceList):
        dist_sum = 0
        for i, item in enumerate(pop):
            if i < len(pop) - 1:
                dist = distanceList.loc[pop[i], pop[i + 1]]
                dist_sum += dis
            else:
                dis = distanceList.loc[pop[i], pop[0]]
                dist_sum += dist
                
        return dist_sum