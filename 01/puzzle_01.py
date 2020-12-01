import fileinput

numbers = []

for line in fileinput.input():
    numbers.append(int(line))

