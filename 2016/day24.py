def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def get_moves(move, maze):
    moves = []
    x = move[0][-1][0]
    y = move[0][-1][1]

    if maze[y - 1][x] != '#' and (x, y - 1) not in move[0]:
        moves.append([move[0] + [(x, y - 1)], move[1] + 1, move[2].copy()])
    if maze[y][x + 1] != '#' and (x + 1, y) not in move[0]:
        moves.append([move[0] + [(x + 1, y)], move[1] + 1, move[2].copy()])
    if maze[y + 1][x] != '#' and (x, y + 1) not in move[0]:
        moves.append([move[0] + [(x, y + 1)], move[1] + 1, move[2].copy()])
    if maze[y][x - 1] != '#' and (x - 1, y) not in move[0]:
        moves.append([move[0] + [(x - 1, y)], move[1] + 1, move[2].copy()])

    return moves

def get_distance(start, end, maze):
    pass

def get_min_moves(coords, maze, targets):
    moves = get_moves(coords, maze)

    while len(moves) > 0:
        move = moves.pop(0)
        x = move[0][-1][0]
        y = move[0][-1][1]
        targets_seen = move[2]

        if isint(maze[y][x]) and int(maze[y][x]) != 0:
            targets_seen.add(int(maze[y][x]))
            move[0] = [move[0][-1]]
            # print('Found {}: {}'.format(maze[y][x], move))
        if targets_seen == set(targets):
            return move[1]

        moves += get_moves(move, maze)

def part_1():
    maze = []
    targets = []
    start = None

    with open('input/day24_input.txt') as f:
        for y, line in enumerate(f):
            row = []
            for x, c in enumerate(line.strip()):
                row.append(c)
                if isint(c):
                    targets.append(int(c))
                    if int(c) == 0:
                        start = (x, y)
            maze.append(row)

    min_moves = get_min_moves([[(start[0], start[1])], 0, {0}], maze, targets)
    print('Part 1: {}'.format(min_moves))

part_1()
