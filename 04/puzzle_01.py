import fileinput
import numpy as np
from pprint import pprint as pp


MATCHES = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
        ]

data = []
for line in fileinput.input():
    if line != '\n':
        data.append(line.rstrip())
    else:
        data.append(line)

document_string = ''
for line in data:
    document_string += line

documents = document_string.split('\n')

correct = 0
for line in documents:
    if all(x in line for x in MATCHES):
        correct += 1

print(correct)

