import fileinput
from collections import Counter

data = [line.rstrip() for line in fileinput.input()]
data.append('')

counter = Counter()
sum_total = 0

for line in data:
    if line == '':
        sum_total += len(set(counter))
        counter = Counter()
    else:
        counter.update(line)

print(sum_total)

