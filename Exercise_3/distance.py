from read_tsp import get_data
import math
a, b = get_data('a280.tsp')
print(a)
print(b)



def cal_dis(args: list, args1: list):
    x1 = args[0]
    y1 = args[1]
    x2 = args1[0]
    y2 = args1[1]
    temp_num = math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)
    dis = math.sqrt(temp_num)
    return dis

a = cal_dis([288,147],[288,137])
print(a)

sum = 0
for i in range(0, b.__len__()-1):
    num = cal_dis(b[i],b[i+1])
    sum+=num

print(sum)