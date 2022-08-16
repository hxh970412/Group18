from read_tsp import get_data


class TspProblem(object):
    def __init__(self, max_num, cross_prob, mut_prob, path):
        self.max_num = max_num  # 最大迭代字数
        self.cross_prob = cross_prob  # 交差概率
        self.mut_prob = mut_prob  # 编译概率
        self.population = []  # 种群
        self.best_path = []  # 存贮每次种群的路径值
        self.fit_array = []  # 存经过筛选之后的染色体
        self.path = path

    # 从文件中读取数据以后，要初始化种群
    def generate_population(self):
        Population = self.population
        # generate population
        return Population  # [[2,4,6,7,1,3,8,9],[5,6,4,3,2,7,8,9],........]

    # 计算城市之间的距离
    def compute_dis(self):
        Best_path = self.best_path
        # 计算城市之间的距离
        return Best_path

    # 筛选
    def fitness(self):
        Fit_array = self.fit_array
        # 筛选方法
        return Fit_array

    def crossover(self):
        Fit_array = self.fit_array
        # 交差方法
        return Fit_array

    def mutation(self):
        Fit_array = self.fit_array
        # 变异方法
        return Fit_array

    def data(self):
        city_id, city_coors = get_data(self.path)
        return city_id, city_coors

if __name__ == '__main__':
