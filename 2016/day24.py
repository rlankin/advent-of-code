def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def get_moves(coords, maze):
    moves = []

    if maze[coords[1] - 1][coords[0]] != '#':
        moves.append((coords[0], coords[1] - 1, coords[2] + 1, coords[3].copy()))
    if maze[coords[1]][coords[0] + 1] != '#':
        moves.append((coords[0] + 1, coords[1], coords[2] + 1, coords[3].copy()))
    if maze[coords[1] + 1][coords[0]] != '#':
        moves.append((coords[0], coords[1] + 1, coords[2] + 1, coords[3].copy()))
    if maze[coords[1]][coords[0] - 1] != '#':
        moves.append((coords[0] - 1, coords[1], coords[2] + 1, coords[3].copy()))

    return moves

def get_min_moves(coords, maze, targets):
    moves = get_moves(coords, maze)

    while len(moves) > 0:
        move = moves.pop(0)
        x = move[0]
        y = move[1]
        steps = move[2]
        targets_seen = move[3]

        if isint(maze[y][x]) and int(maze[y][x]) != 0:
            targets_seen.add(int(maze[y][x]))
            # print('Found {}: {}'.format(maze[y][x], move))
        if targets_seen == set(targets):
            return steps

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
                    # targets[(x, y)] = int(c)
                    targets.append(int(c))
                    if int(c) == 0:
                        start = (x, y)
            maze.append(row)
    
    min_moves = get_min_moves((start[0], start[1], 0, {0}), maze, targets)
    print('Part 1: {}'.format(min_moves))

part_1()
