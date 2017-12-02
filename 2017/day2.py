def part_1():
    with open('input/day2_input') as f:
        s = 0
        for line in f:
            row = [int(x) for x in line.split('\t')]
            s += (max(row) - min(row))

        print('Part 1: {}'.format(s))

def part_2():
    with open('input/day2_input') as f:
        s = 0

        for line in f:
            row = [int(x) for x in line.split('\t')]
            for x in row:
                for y in row:
                    if x != y and x % y == 0:
                        s += int(x / y)

        print('Part 2: {}'.format(s))

part_1()
part_2()
