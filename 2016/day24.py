import itertools

def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def get_moves(move, maze):
    moves = []
    x = move[0][0]
    y = move[0][1]

    if maze[y - 1][x] != '#':
        moves.append(((x, y - 1), move[1] + 1))
    if maze[y][x + 1] != '#':
        moves.append(((x + 1, y), move[1] + 1))
    if maze[y + 1][x] != '#':
        moves.append(((x, y + 1), move[1] + 1))
    if maze[y][x - 1] != '#':
        moves.append(((x - 1, y), move[1] + 1))

    return moves

def get_distance(start, end, maze):
    maze_dist = [[-1] * len(maze[0]) for _ in range(len(maze))]
    maze_dist[start[0][1]][start[0][0]] = 0
    moves = get_moves(start, maze)

    while len(moves) > 0:
        move = moves.pop(0)
        x = move[0][0]
        y = move[0][1]

        if maze_dist[y][x] != -1:
            continue

        if x == end[0] and y == end[1]:
            return move[1]

        maze_dist[y][x] = move[1]

        moves += get_moves(move, maze)

def build_distance_matrix(targets, maze):
    dist_matrix = [[-1] * len(targets) for _ in range(len(targets))]
    for start in range(len(targets)):
        for end in range(start, len(targets)):
            dist = 0 if start == end else get_distance((targets[start], 0), targets[end], maze)
            dist_matrix[start][end] = dist_matrix[end][start] = dist

    return dist_matrix

def get_min_steps(dist_matrix, return_to_start = False):
    min_steps = -1
    for path in itertools.permutations(range(len(dist_matrix))):
        if path[0] == 0:
            steps = 0

            for i in range(1, len(path)):
                steps += dist_matrix[path[i]][path[i - 1]]
            if return_to_start:
                steps += dist_matrix[path[i]][0]

            if steps < min_steps or min_steps == -1:
                min_steps = steps

    return min_steps

def part_1():
    maze = []
    targets = {}

    with open('input/day24_input.txt') as f:
        for y, line in enumerate(f):
            row = []
            for x, c in enumerate(line.strip()):
                row.append(c)
                if isint(c):
                    targets[int(c)] = (x, y)
            maze.append(row)

    dist_matrix = build_distance_matrix(targets, maze)
    min_steps = get_min_steps(dist_matrix)

    print('Part 1: {}'.format(min_steps))

def part_2():
    maze = []
    targets = {}

    with open('input/day24_input.txt') as f:
        for y, line in enumerate(f):
            row = []
            for x, c in enumerate(line.strip()):
                row.append(c)
                if isint(c):
                    targets[int(c)] = (x, y)
            maze.append(row)

    dist_matrix = build_distance_matrix(targets, maze)
    min_steps = get_min_steps(dist_matrix, return_to_start = True)

    print('Part 2: {}'.format(min_steps))

part_1()
part_2()
