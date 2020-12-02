import fileinput
from pprint import pprint as pp

puzzle_input = [line.rstrip() for line in fileinput.input()]
database = []

for line in puzzle_input:
    occurence_count = (
            int(line[0:line.find('-')]),
            int(line[line.find('-') + 1:line.find(' ')])
            )

    letter = line[line.find(' ') + 1]
    password = line[line.rfind(' ') + 1:]

    database.append(
            (
                occurence_count,
                letter,
                password
                )
            )

correct_count = 0

for (a, b), x, y in database:
    if y.count(x) >= a and y.count(x) <= b:
        correct_count += 1

print(correct_count)
