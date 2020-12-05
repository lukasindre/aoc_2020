import fileinput

seat_ids = set()
for line in [line.rstrip() for line in fileinput.input()]:
    row = col = 0
    for letter in line:
        if letter == 'F':
            row = row << 1
        elif letter == 'B':
            row = row << 1 | 1
        elif letter == 'L':
            col <<= 1
        elif letter == 'R':
            col = col << 1 | 1

    seat_ids.add(row * 8 + col)

print(max(seat_ids))
