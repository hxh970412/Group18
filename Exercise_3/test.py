from IndividualAndPopulation import IndividualAndPopulation



data = [(37.0, 52.0), (49.0, 49.0), (52.0, 64.0), (20.0, 26.0), (40.0, 30.0), (21.0, 47.0), (17.0, 63.0), (31.0, 62.0), (52.0, 33.0), (51.0, 21.0), (42.0, 41.0), (31.0, 32.0), (5.0, 25.0), (12.0, 42.0), (36.0, 16.0), (52.0, 41.0), (27.0, 23.0), (17.0, 33.0), (13.0, 13.0), (57.0, 58.0), (62.0, 42.0), (42.0, 57.0), (16.0, 57.0), (8.0, 52.0), (7.0, 38.0), (27.0, 68.0), (30.0, 48.0), (43.0, 67.0), (58.0, 48.0), (58.0, 27.0), (37.0, 69.0), (38.0, 46.0), (46.0, 10.0), (61.0, 33.0), (62.0, 63.0), (63.0, 69.0), (32.0, 22.0), (45.0, 35.0), (59.0, 15.0), (5.0, 6.0), (10.0, 17.0), (21.0, 10.0), (5.0, 64.0), (30.0, 15.0), (39.0, 10.0), (32.0, 39.0), (25.0, 32.0), (25.0, 55.0), (48.0, 28.0), (56.0, 37.0), (30.0, 40.0)]
pop = [18, 39, 1, 43, 10, 36, 7, 21, 6, 12, 20, 27, 24, 0, 38, 44, 9, 32, 16, 15, 40, 13, 26, 11, 4, 45, 50, 22, 19, 2, 41, 47, 48, 3, 49, 37, 31, 35, 42, 33, 29, 5, 25, 30, 17, 23, 14, 28, 46, 8, 34]
# print(IndividualAndPopulation.makeTheMatrix(data))
print(IndividualAndPopulation.makePopulation(data, 5))
print(IndividualAndPopulation.calIndDist(pop, IndividualAndPopulation.makeTheMatrix(data)))