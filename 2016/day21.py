import itertools

SWAP_POS = 0
SWAP_LET = 1
ROT_LEFT = 2
ROT_RIGHT = 3
ROT_POS = 4
REVERSE = 5
MOVE = 6

def parse_operation(op_str, reverse = False):
    op = None
    p = op_str.strip().split()

    if p[0] == 'swap':
        if p[1] == 'position':
            op = (SWAP_POS, int(p[2]), int(p[5]))
        elif p[1] == 'letter':
            op = (SWAP_LET, p[2], p[5])
    elif p[0] == 'rotate':
        if p[1] == 'left':
            op = (ROT_LEFT, int(p[2]))
        elif p[1] == 'right':
            op = (ROT_RIGHT, int(p[2]))
        elif p[1] == 'based':
            op = (ROT_POS, p[6], 0)
    elif p[0] == 'reverse':
        op = (REVERSE, int(p[2]), int(p[4]))
    elif p[0] == 'move':
        op = (MOVE, int(p[2]), int(p[5]))
    else:
        print('ERROR: ' + op_str)

    return op

def scramble_password(password, operations):
    results = []
    s = list(password)

    for op in operations:
        if op[0] == SWAP_POS:
            s[op[1]], s[op[2]] = s[op[2]], s[op[1]]
        elif op[0] == SWAP_LET:
            x_index = s.index(op[1])
            y_index = s.index(op[2])
            s[x_index], s[y_index] = s[y_index], s[x_index]
        elif op[0] == ROT_LEFT:
            for i in range(op[1]):
                s.append(s.pop(0))
        elif op[0] == ROT_RIGHT:
            for i in range(op[1]):
                s.insert(0, s.pop())
        elif op[0] == ROT_POS:
            index = s.index(op[1])
            for i in range(index + 1):
                s.insert(0, s.pop())
            if index >= 4:
                s.insert(0, s.pop())
        elif op[0] == REVERSE:
            s[op[1]:op[2] + 1] = (s[op[2]:op[1] - 1:-1] if op[1] - 1 > -1 else s[op[2]::-1])
        elif op[0] == MOVE:
            s.insert(op[2], s.pop(op[1]))

    return ''.join(s)

def part_1():
    operations = []
    password = 'abcdefgh'

    with open('input/day21_input.txt', 'r') as f:
        for op_str in f:
            operations.append(parse_operation(op_str))

    print('Part 1: {}'.format(scramble_password(password, operations)))

def part_2():
    operations = []
    scrambled = 'fbgdceah'
    password = None

    with open('input/day21_input.txt', 'r') as f:
        for op_str in f:
            operations.append(parse_operation(op_str))

    for p in itertools.permutations(scrambled):
        if scramble_password(p, operations) == scrambled:
            password = ''.join(p)
            break

    print('Part 2: {}'.format(password))

part_1()
part_2()
