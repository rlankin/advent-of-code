def calc_num_jumps(jumps, offset_func):
    i = 0
    steps = 0
    while 0 <= i < len(jumps):
        offset = offset_func(jumps[i])
        jumps[i] += offset
        i += jumps[i] - offset
        steps += 1
    return steps

def part_1():
    jumps = []
    with open('input/day5_input', 'r') as f:
        jumps = [int(x) for x in f]

    print('Part 1: {}'.format(calc_num_jumps(jumps, lambda j: 1)))

def part_2():
    jumps = []
    with open('input/day5_input', 'r') as f:
        jumps = [int(x) for x in f]
    # jumps = [0, 3, 0, 1, -3]

    print('Part 2: {}'.format(calc_num_jumps(jumps, lambda j: -1 if j >= 3 else 1)))

part_1()
part_2()
