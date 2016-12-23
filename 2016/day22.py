import itertools
import re

SIZE = 0
USED = 1
AVAIL = 2
USE_PCT = 3
NODE_RE = re.compile('/dev/grid/node-x([0-9]+)-y([0-9]+)\s*([0-9]+)T\s*([0-9]+)T\s*([0-9]+)T\s*([0-9]+)%')

def part_1():
    nodes = {}
    viable_pairs = 0

    with open('input/day22_input.txt', 'r') as f:
        # Discard first two lines of input
        f.readline()
        f.readline()

        for line in f:
            match = NODE_RE.match(line.strip())
            nodes[(int(match.group(1)), int(match.group(2)))] = (int(match.group(3)), int(match.group(4)), int(match.group(5)), int(match.group(6)))

    for pair in itertools.combinations(nodes, 2):
        a = nodes[pair[0]]
        b = nodes[pair[1]]
        if a[USED] > 0 and a[USED] <= b[AVAIL] \
            or b[USED] > 0 and b[USED] <= a[AVAIL]:
            viable_pairs += 1

    print('Part 1: {}'.format(viable_pairs))

def part_2():
    nodes = []
    empty_avail = 0

    with open('input/day22_input.txt', 'r') as f:
        # Discard first two lines of input
        f.readline()
        f.readline()

        for line in f:
            match = NODE_RE.match(line.strip())
            nodes.append([int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)), int(match.group(6))])
            if int(match.group(4)) == 0:
                empty_avail = int(match.group(5))

    # Sort by y, x
    nodes.sort(key = lambda n: (n[1], n[0]))

    max_x = nodes[-1][0]

    print('Part 2:')
    line = ''
    for node in nodes:
        char = '. '
        if node[3] > empty_avail:
            char = '# '
        elif node[3] == 0:
            char = '_ '

        line += char

        if node[0] == max_x:
            print(line)
            line = ''

part_1()
part_2()
