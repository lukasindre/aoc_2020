import fileinput
from pprint import pprint as pp


data = [int(line.rstrip()) for line in fileinput.input()]

max_builtin_joltage = max(set(data)) + 3
data.append(0)
data.append(max_builtin_joltage)
data.sort()

one_jolt_diff = 0
three_jolt_diff = 0

counter = 0
while counter < len(data) - 1:
    if data[counter + 1] - data[counter] == 1:
        one_jolt_diff += 1
    elif data[counter + 1] - data[counter] == 3:
        three_jolt_diff += 1

    counter += 1

print(one_jolt_diff*three_jolt_diff)
