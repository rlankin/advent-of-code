def calc_num_jumps(jumps, offset_func):
    jumps_copy = list(jumps)
    i = 0
    steps = 0
    while 0 <= i < len(jumps_copy):
        source = i
        i += jumps_copy[i]
        jumps_copy[source] += offset_func(jumps_copy[source])
        steps += 1
    return steps

jumps = []
with open('input/day5_input', 'r') as f:
    jumps = [int(x) for x in f]

print('Part 1: {}'.format(calc_num_jumps(jumps, lambda j: 1)))
print('Part 2: {}'.format(calc_num_jumps(jumps, lambda j: -1 if j >= 3 else 1)))
