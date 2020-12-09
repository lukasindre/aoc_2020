import fileinput
from itertools import combinations
from pprint import pprint as pp

ANSWER = 85848519

data = [int(line.rstrip()) for line in fileinput.input()]

subs = [data[i:i+j] for i in range(0,len(data)) for j in range(1,len(data)-i+1)]

for sub in subs:
    if sum(sub) == ANSWER and len(sub) > 1:
        print(max(set(sub)) + min(set(sub)))
        break

