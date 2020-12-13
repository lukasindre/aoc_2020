import fileinput
from pprint import pprint as pp


def price_is_right(timestamp, bus_id):
    bus_stamp = 0
    while 1 == 1:
        bus_stamp += bus_id
        if bus_stamp >= timestamp:
            break

    return bus_stamp


data = [line.rstrip() for line in fileinput.input()]
earliest_timestamp = int(data[0])
bus_ids = [int(bus_id) for bus_id in data[1].split(',') if bus_id != 'x']

bus_stamps = {}
for bus_id in bus_ids:
    bus_stamps[bus_id] = price_is_right(earliest_timestamp, bus_id)

min_time = float('inf')
for key in bus_stamps:
    if bus_stamps[key] < min_time:
        min_time = bus_stamps[key]

for x, y in bus_stamps.items():
    if y == min_time:
        print((min_time - earliest_timestamp) * x)
