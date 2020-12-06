import fileinput
from collections import Counter

data = [line.rstrip() for line in fileinput.input()]
data.append("")

counter = Counter()
sum_total = 0
group_size = 0

for line in data:
    if line == '':
        sum_total += len(set([question for question in counter.items() if question[1] == group_size]))
        counter = Counter()
        group_size = 0
    else:
        group_size += 1
        counter.update(line)

print(sum_total)
