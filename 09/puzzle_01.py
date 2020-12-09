import fileinput
from itertools import combinations
from pprint import pprint as pp

data = [int(line.rstrip()) for line in fileinput.input()]

counter = 25

while counter < len(data):
    combos = list(combinations(data[counter - 25:counter], 2))
    if all(combo[0] + combo[1] != data[counter] for combo in combos):
        print(data[counter])
        break
    else:
        counter += 1

