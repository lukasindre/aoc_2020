import fileinput
import numpy


def get_tree_encounters(x, y, tm, row_count, row_width):
    a = 0
    b = 0
    tree_count = 0
    while b < row_count:
        if a >= row_width:
            a -= row_width
        if tm[b][a] == '#':
            tree_count += 1

        a += x
        b += y

    return tree_count


travel_map = [line.rstrip() for line in fileinput.input()]
rows = len(travel_map)
width_of_row = len(travel_map[0])
tree_count = 0

slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
        ]

counts = []
for (x, y) in slopes:
    counts.append(
            get_tree_encounters(
                x=x,
                y=y,
                tm=travel_map,
                row_count=rows,
                row_width=width_of_row
                )
            )

print(numpy.prod(counts))

