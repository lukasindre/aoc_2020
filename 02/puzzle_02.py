import fileinput
from pprint import pprint as pp

puzzle_input = [line.rstrip() for line in fileinput.input()]
database = []

for line in puzzle_input:
    positions = (
            int(line[0:line.find('-')]),
            int(line[line.find('-') + 1:line.find(' ')])
            )

    letter = line[line.find(' ') + 1]
    password = line[line.rfind(' ') + 1:]

    database.append(
            (
                positions,
                letter,
                password
                )
            )

correct_count = 0

for (a, b), x, y in database:
    if y[a - 1] == x and y[b - 1] == x:
        next
    elif y[a - 1] == x or y[b - 1] == x:
        correct_count += 1

print(correct_count)
