import tsplib95 as tsp


def get_data(path: str):
    problem = tsp.loaders.load(path)
    city_id = list(problem.get_nodes())
    nodes_coord = []  # 城市坐标
    for i in range(1, city_id.__len__() + 1):
        nodes_coord.append(problem.node_coords[i])

    return city_id, nodes_coord


a, b = get_data('a280.tsp')
print(a)
print(b)

