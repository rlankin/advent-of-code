cities = {}

with open("day9_input.txt") as f:
    for path in f:
        parsed = path.rstrip().split(" ")

        if parsed[0] not in cities:
            cities[parsed[0]] = {}
        cities[parsed[0]][parsed[2]] = int(parsed[4])

        if parsed[2] not in cities:
            cities[parsed[2]] = {}
        cities[parsed[2]][parsed[0]] = int(parsed[4])

def get_path_length(dist, curr, unvisited, path_lengths):
    if not unvisited:
        path_lengths.add(dist)

    for city in unvisited:
        get_path_length(dist + cities[curr][city], city, [c for c in unvisited if c != city], path_lengths)

def part_1():
    unvisited = [city for city in cities]
    path_lengths = set()
    for city in unvisited:
        get_path_length(0, city, [c for c in unvisited if c != city], path_lengths)

    print("Part 1: " + str(min(path_lengths)))

def part_2():
    unvisited = [city for city in cities]
    path_lengths = set()
    for city in unvisited:
        get_path_length(0, city, [c for c in unvisited if c != city], path_lengths)

    print("Part 1: " + str(max(path_lengths)))

part_1()
part_2()
