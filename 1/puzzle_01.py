import fileinput
import itertools

numbers = [int(line) for line in fileinput.input()]

for x, y in itertools.combinations(numbers, 2):
    if x + y == 2020:
        print(x * y)

