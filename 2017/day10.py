from functools import reduce

def knot_hash_round(lst, lengths, pos, skip):
    for l in lengths:
        rev = list(reversed([lst[(pos + i) % len(lst)] for i in range(l)]))
        for i in range(l):
            lst[(pos + i) % len(lst)] = rev[i]
        pos += (l + skip) % len(lst)
        skip += 1
    return pos, skip

def part_1():
    lengths = []
    with open('input/day10_input', 'r') as f:
        lengths = [int(l) for l in f.readline().strip().split(',')]

    lst = [i for i in range(256)]
    pos = 0
    skip = 0

    pos, skip = knot_hash_round(lst, lengths, pos, skip)

    print('Part 1: {}'.format(lst[0] * lst[1]))

def part_2():
    lengths = []
    with open('input/day10_input', 'r') as f:
        lengths = [ord(l) for l in f.readline().strip()] + [17, 31, 73, 47, 23]

    lst = [i for i in range(256)]
    pos = 0
    skip = 0

    for r in range(64):
        pos, skip = knot_hash_round(lst, lengths, pos, skip)

    dense_hash = [reduce(lambda x, y: x ^ y, lst[i*16:(i+1)*16]) for i in range(16)]

    print('Part 2: {}'.format(''.join(format(i, '02x') for i in dense_hash)))

part_1()
part_2()
