import fileinput
from pprint import pprint as pp

data = []
for line in fileinput.input():
    if line != '\n':
        data.append(line.rstrip())
    else:
        data.append(line)

answers_string = ''
for line in data:
    answers_string += line

answers = answers_string.split('\n')

sum = 0
for group_answers in answers:
    group_set = set([])
    for answer in group_answers:
        group_set.add(answer)

    sum += len(group_set)

print(sum)

