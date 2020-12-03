import fileinput


travel_map = [line.rstrip() for line in fileinput.input()]

rows = len(travel_map)
width_of_row = len(travel_map[0])

tree_count = 0
x = 0
y = 0

# need to find something that deals with when x is greater than the size of a row
# from input and how to get that to repeat...

while y < rows:
    if x >= width_of_row:
         x -= width_of_row
    if travel_map[y][x] == '#':
        tree_count += 1

    x += 3
    y += 1

print(tree_count)

