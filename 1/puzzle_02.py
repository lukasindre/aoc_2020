import fileinput
import itertools

numbers = []

for line in fileinput.input():
    numbers.append(int(line))

for combination in itertools.combinations(numbers, 3):
    if combination[0] + combination[1] + combination[2] == 2020:
        print(combination[0] * combination[1] * combination[2])

