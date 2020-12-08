import fileinput
from collections import Counter
from pprint import pprint as pp


def send_it(rules):
    i = 0
    accumulator = 0
    actions = []
   
    while i < len(rules):
        actions.append(i)
        if list(dict(Counter(actions)).values()).count(2) >= 1:
            print(accumulator)
            break
        elif rules[i][0] == 'acc':
            accumulator += int(rules[i][1])
            i += 1
        elif rules[i][0] == 'jmp':
            i += int(rules[i][1])
        else:
            i += 1

data = [line.rstrip().split() for line in fileinput.input()]

send_it(data)
