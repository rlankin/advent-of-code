UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

step = {
    UP: lambda pos: [pos[0] - 1, pos[1]],
    RIGHT: lambda pos: [pos[0], pos[1] + 1],
    DOWN: lambda pos: [pos[0] + 1, pos[1]],
    LEFT: lambda pos: [pos[0], pos[1] - 1],
}

def char_at(diagram, pos):
    return diagram[pos[0]][pos[1]] if 0 <= pos[0] < len(diagram) and 0 <= pos[1] < len(diagram[pos[0]]) else ''

def is_valid_move(pos, d, p):
    line_types = ['|', '+'] if d == UP or d == DOWN else ['-', '+']
    ns = step[d](pos)
    return (d != p
        and (char_at(diagram, ns) in line_types or char_at(diagram, ns).isalpha()))

diagram = []
with open('input/day19_test', 'r') as f:
    for line in f:
        diagram.append([c for c in line[:-1]])

pos = [0, len(diagram[0]) - 1]
d = DOWN
letters = []

# while 0 <= pos[0] < len(diagram) and 0 <= pos[1] < len(diagram[pos[0]]):
while True:
    pos = step[d](pos)
    if char_at(diagram, pos).isalpha():
        letters.append(char_at(diagram, pos))
        if not is_valid_move(pos, UP, d) and not is_valid_move(pos, RIGHT, d) and not is_valid_move(pos, DOWN, d) and not is_valid_move(pos, LEFT, d):
            break
    if diagram[pos[0]][pos[1]] == '+':
        ns = step[UP](pos)
        if d != DOWN and (char_at(diagram, ns) == '|' or char_at(diagram, ns).isalpha()):
            d = UP
            continue
        ns = step[RIGHT](pos)
        if d != LEFT and (char_at(diagram, ns) == '-' or char_at(diagram, ns).isalpha()):
            d = RIGHT
            continue
        ns = step[DOWN](pos)
        if d != UP and (char_at(diagram, ns) == '|' or char_at(diagram, ns).isalpha()):
            d = DOWN
            continue
        ns = step[LEFT](pos)
        if d != RIGHT and (char_at(diagram, ns) == '-' or char_at(diagram, ns).isalpha()):
            d = LEFT
            continue
        break

print('Part 1: {}'.format(''.join(letters)))
