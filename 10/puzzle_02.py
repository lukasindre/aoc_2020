import fileinput
from itertools import groupby
from operator import sub
from math import prod

data = [int(line) for line in fileinput.input()]
data.sort()

count_data = [[a, len(list(b))] for a, b in groupby(sub(*pair) for pair in zip(data, [0] + data))] + [[3, 1]]

maps = {
        1: 1,
        2: 2,
        3: 4,
        4: 7
        }

print(prod(maps[num[1]] for num in count_data if num[0] == 1))
