LITERS_TO_STORE = 150
CONTAINERS = []

with open("input/day17_input.txt") as f:
    for c in f:
        CONTAINERS.append(int(c.rstrip()))
CONTAINERS.sort(reverse = True)

def get_combinations(amount, remaining, curr_set):
    if amount == 0:
        return [curr_set]

    sets = []
    for i, container in enumerate(remaining):
        if container <= amount:
            new_set = list(curr_set) + [container]
            sets += get_combinations(amount - container, remaining[i + 1:], new_set)

    return sets

def part_1():
    combinations = get_combinations(LITERS_TO_STORE, CONTAINERS, [])
    print("Part 1: " + str(len(combinations)))

def part_2():
    combinations = get_combinations(LITERS_TO_STORE, CONTAINERS, [])
    min_len = min([len(c) for c in combinations])
    min_len_com = len([c for c in combinations if len(c) == min_len])
    print("Part 2: " + str(min_len_com))

part_1()
part_2()
