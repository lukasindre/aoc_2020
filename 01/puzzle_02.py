import fileinput
import itertools

numbers = [int(line) for line in fileinput.input()]

for x, y, z in itertools.combinations(numbers, 3):
    if x + y + z == 2020:
        print(x * y * z)

