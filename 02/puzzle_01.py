import fileinput
from pprint import pprint as pp

puzzle_input = [line.rstrip() for line in fileinput.input()]
database = []

for line in puzzle_input:
    occurence_count = (
            line[0:line.find('-')],
            line[line.find('-') + 1:line.find(' ')]
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

pp(database)

