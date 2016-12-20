def part_1():
    blacklist = []

    with open('input/day20_input.txt', 'r') as f:
        for rng in f:
            parsed = rng.split('-')
            blacklist.append((int(parsed[0]), int(parsed[1])))

    blacklist.sort(key = lambda rng: rng[0])

    lowest = None
    for rng in blacklist:
        if lowest and lowest < rng[0]:
            break
        lowest = rng[1] + 1

    print('Part 1: {}'.format(lowest))

def part_2():
    blacklist = []

    with open('input/day20_input.txt', 'r') as f:
        for rng in f:
            parsed = rng.split('-')
            blacklist.append((int(parsed[0]), int(parsed[1])))

    blacklist.sort(key = lambda rng: rng[0])

    allowed = 0
    high = blacklist[0][1]
    for i in range(1, len(blacklist)):
        if blacklist[i][0] > high:
            allowed += blacklist[i][0] - high - 1

        if blacklist[i][1] > high:
            high = blacklist[i][1]

    print('Part 2: {}'.format(allowed))

part_1()
part_2()
