import fileinput
from collections import Counter
from pprint import pprint as pp

data = [line.rstrip().split() for line in fileinput.input()]

actions = []
accumulator = 0
i = 0


while i < len(data):
    actions.append(i)
    if list(dict(Counter(actions)).values()).count(2) >= 1:
        print(accumulator)
        break
    elif data[i][0] == 'acc':
        accumulator += int(data[i][1])
        i += 1
    elif data[i][0] == 'jmp':
        i += int(data[i][1])
    else:
        i += 1

