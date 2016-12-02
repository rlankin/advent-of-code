import json

parsed_json = None
with open('input/day12_input.txt', 'r') as f:
    parsed_json = json.loads(f.read())

def get_sum(e):
    if isinstance(e, int):
        return e
    elif isinstance(e, list):
        return sum([get_sum(e2) for e2 in e])
    elif isinstance(e, dict):
        return sum([get_sum(v) for (k, v) in e.items()])

    return 0

def get_sum_no_red(e):
    if isinstance(e, int):
        return e
    elif isinstance(e, list):
        return sum([get_sum_no_red(e2) for e2 in e])
    elif isinstance(e, dict):
        values = [v for (k, v) in e.items()]
        if "red" not in values:
            return sum([get_sum_no_red(v) for v in values])

    return 0

def part_1():
    s = get_sum(parsed_json)
    print("Part 1: " + str(s))

def part_2():
    s = get_sum_no_red(parsed_json)
    print("Part 2: " + str(s))

part_1()
part_2()
