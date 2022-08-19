import numpy as np
import pandas as pd


class read_tsp:
    def get_data(path): # read the tsp file and make a list
        df = pd.read_csv(path, sep=" ", skiprows=6, header=None)
        node = list(df[0][0:-1])
        num_points = len(node)
        city_x = np.array(df[1][0:-1])
        city_y = np.array(df[2][0:-1])
        city_location = list(zip(city_x, city_y))
        return city_location
