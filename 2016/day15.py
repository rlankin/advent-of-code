import re

DISC_RE = re.compile('.* ([0-9]+) positions;.*position ([0-9]+).*')

def drop_capsule(discs, time):
    for disc in discs:
        time += 1
        if (disc[0] + time) % disc[1] != 0:
            return False

    return True

def part_1():
    discs = []

    with open('input/day15_input.txt', 'r') as f:
        for line in f:
            match = DISC_RE.match(line)
            discs.append([int(match.group(2)), int(match.group(1))])

    time = 0
    while not drop_capsule(discs, time):
        time += 1

    print('Part 1: {}'.format(time))

def part_2():
    discs = []

    with open('input/day15_input.txt', 'r') as f:
        for line in f:
            match = DISC_RE.match(line)
            discs.append([int(match.group(2)), int(match.group(1))])

    discs.append([0, 11])

    time = 0
    while not drop_capsule(discs, time):
        time += 1

    print('Part 2: {}'.format(time))

part_1()
part_2()
