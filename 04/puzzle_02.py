import fileinput
import re
import numpy as np
import json
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

EYE_COLOR = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
        ]

HEX = re.compile(r"#[0-9a-f]{6}")

def split_string(word):
    return [character for character in word]

data = []
for line in fileinput.input():
    if line != '\n':
        data.append(line.rstrip())
    else:
        data.append(line)

document_string = ''
for line in data:
    document_string += f" {line}"

documents = document_string.split('\n')

data = []
for line in documents:
    new_line = line.lstrip().rstrip()
    data.append(new_line)
    
attr_list = []

for line in data:
    attr_list.append(line.split(' '))


new_attr_list = []
for passport in attr_list:
    new_pass = []
    new_dict = {}
    for attr in passport:
        placeholder = split_string(attr)
        placeholder.insert(len(placeholder), '"')
        placeholder.insert(len(placeholder), "}")
        placeholder.insert(0, '"')
        placeholder.insert(0, '{')
        placeholder.insert(5, '"')
        placeholder.insert(7, '"')
        s = ''
        new_pass.append(s.join(placeholder))
    new_attr_list.append(new_pass)

pass_list = []
for passport in new_attr_list:
    merger = {}
    pass_dict = []
    for attr in passport:
        merger.update(json.loads(attr))
    pass_list.append(merger)

counter = 0
for passport in pass_list:
    if set(MATCHES).issubset(set(list(passport.keys()))):
        height = passport['hgt']
        birth_year = int(passport['byr'])
        issue_year = int(passport['iyr'])
        expire_year = int(passport['eyr'])
        hair_color = passport['hcl']
        eye_color = passport['ecl']
        passport_id = passport['pid']

        height_valid = False
        birth_year_valid = False
        issue_year_valid = False
        expire_year_valid = False
        hair_color_valid = False
        eye_color_valid = False
        passport_id_valid = False
        
        if height[-2:] == 'cm':
            if int(height[:len(height) - 2]) >= 150 and int(height[:len(height) - 2]) <= 193:
                height_valid = True
        elif height[-2:] == 'in':
            if int(height[:len(height) - 2]) >= 59 and int(height[:len(height) - 2]) <=76:
                height_valid = True

        if len(str(birth_year)) == 4 and birth_year >= 1920 and birth_year <= 2002:
            birth_year_valid = True

        if len(str(issue_year)) == 4 and issue_year >= 2010 and issue_year <= 2020:
            issue_year_valid = True
        
        if len(str(expire_year)) == 4 and expire_year >= 2020 and expire_year <= 2030:
            expire_year_valid = True

        if HEX.fullmatch('hair_color'):
            hair_color_valid = True

        if eye_color in EYE_COLOR:
            eye_color_valid = True

        if len(passport_id) == 9:
            passport_id_valid = True

        print(hair_color)
        if height_valid and birth_year_valid and issue_year_valid and expire_year_valid and hair_color_valid and eye_color_valid and passport_id_valid:
            counter += 1

    else:
        next

print(counter)
