import fileinput
from pprint import pprint as pp


def split_list(a_list):
    half = len(a_list)//2
    return [a_list[:half], a_list[half:]]

def reduce_list(letter, seats, which_type):
    if which_type == 'row':
        if letter == 'F':
            return split_list(seats)[0]
        else:
            return split_list(seats)[1]
    else:
        if letter == 'L':
            return split_list(seats)[0]
        else:
            return split_list(seats)[1]


passes = [line.rstrip() for line in fileinput.input()]

seat_ids = []
for line in passes:
    rows = list(range(0, 128))
    columns = list(range(0, 8))
    reduced_list = None
    row_letters = line[:7]
    column_letters = line[7:]

    for letter in row_letters:
        rows = reduce_list(letter, rows, 'row')

    row_number = rows[0]

    for letter in column_letters:
        columns = reduce_list(letter, columns, '')

    column_number = columns[0]

    seat_ids.append(row_number * 8 + column_number)

seat_ids = list(set(seat_ids))

pp(seat_ids)

for seat_id in range(len(seat_ids) - 1):
    if seat_ids[seat_id + 1] - seat_ids[seat_id] != 1:
        print(seat_ids[seat_id])

