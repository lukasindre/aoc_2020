import fileinput
from pprint import pprint as pp


def send_it(rules):
    i = 0
    accumulator = 0
    stop_loop_count = 0
   
    while stop_loop_count < len(rules):
        if i == len(rules):
            print(accumulator)
            break
        elif rules[i][0] == 'acc':
            accumulator += int(rules[i][1])
            i += 1
        elif rules[i][0] == 'jmp':
            i += int(rules[i][1])
        else:
            i += 1

        stop_loop_count += 1

data = [line.rstrip().split() for line in fileinput.input()]

for counter in range(len(data)):
    this_try = data
    
    if data[counter][0] == 'acc':
        continue
    
    if data[counter][0] == 'jmp':
        this_try[counter][0] = 'nop'
    elif data[counter][0] == 'nop':
        this_try[counter][0] = 'jmp'

    send_it(this_try)

