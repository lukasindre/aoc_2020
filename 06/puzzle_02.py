import fileinput
from itertools import groupby
from collections import Counter
from pprint import pprint as pp


def common_chars(a_list):
    counts = Counter(a_list[0])

    for word in a_list:
        counts &= Counter(word)
    
    solution = []
    for letter, count in counts.items():
        solution += [letter] * count

    return solution


data = []
for line in fileinput.input():
    if line != '\n':
        data.append(line.rstrip())
    else:
        data.append(line)

data = [line.rstrip() for line in data]

grouped_data = []

size = len(data)
idx_list = [idx + 1 for idx, val in enumerate(data) if val == '']

grouped_data = [
        data[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))]

for group in grouped_data:
    if '' in group:
        group.remove('')

sum = 0
for group in grouped_data:
    chars = common_chars(group)
    sum += len(chars)

print(sum)
