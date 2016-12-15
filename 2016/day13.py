FAV_NUM = 1364
DESTINATION = (31, 39)

def print_maze(maze, path = None):
    for y, row in enumerate(maze):
        for x, v in enumerate(row):
            symbol = '#'
            if not v:
                symbol = 'O' if path and (x, y) in path else '.'
            print(symbol, end = '')
        print()
    print()

def calculate_space(x, y):
    """Return 0 for an empty space, 1 for a wall"""
    value = (x*x + 3*x + 2*x*y + y + y*y) + FAV_NUM
    return sum(1 for b in bin(value) if b == '1') % 2

def expand_maze(maze, step):
    if step[1] >= len(maze):
        maze.append([calculate_space(x, step[1]) for x in range(len(maze[0]))])

    if step[0] >= len(maze[0]):
        for y, row in enumerate(maze):
            row.append(calculate_space(step[0], y))

def path_to_destination(path, maze, step_totals):
    step = path[-1]

    expand_maze(maze, step)

    if step[0] < 0 or step[1] < 0 or maze[step[1]][step[0]] == 1 \
        or (len(step_totals) > 0 and len(path) > min(step_totals)) \
        or step in path[:-1]:
        # Invalid move, path too long, or looped back around
        return

    if step[0] == DESTINATION[0] and step[1] == DESTINATION[1]:
        step_totals.append(len(path) - 1)
        # print_maze(maze, path = path)

    # Move up
    path.append((step[0], step[1] - 1))
    path_to_destination(path, maze, step_totals)
    path.pop()

    # Move right
    path.append((step[0] + 1, step[1]))
    path_to_destination(path, maze, step_totals)
    path.pop()

    # Move down
    path.append((step[0], step[1] + 1))
    path_to_destination(path, maze, step_totals)
    path.pop()

    # Move left
    path.append((step[0] - 1, step[1]))
    path_to_destination(path, maze, step_totals)
    path.pop()

def count_locations(path, maze, locations):
    step = path[-1]

    expand_maze(maze, step)

    if step[0] < 0 or step[1] < 0 or maze[step[1]][step[0]] == 1 \
        or len(path) > 51 \
        or step in path[:-1]:
        # Invalid move, path too long, or looped back around
        return

    locations.add(step)

    # Move up
    path.append((step[0], step[1] - 1))
    count_locations(path, maze, locations)
    path.pop()

    # Move right
    path.append((step[0] + 1, step[1]))
    count_locations(path, maze, locations)
    path.pop()

    # Move down
    path.append((step[0], step[1] + 1))
    count_locations(path, maze, locations)
    path.pop()

    # Move left
    path.append((step[0] - 1, step[1]))
    count_locations(path, maze, locations)
    path.pop()

def part_1():
    maze = [[0] * 2 for y in range(2)]

    # Initialize maze
    for y in range(2):
        for x in range(2):
            maze[y][x] = calculate_space(x, y)

    step_totals = []
    path_to_destination([(1, 1)], maze, step_totals)

    print('Part 1: {}'.format(min(step_totals)))

def part_2():
    maze = [[0] * 2 for y in range(2)]

    # Initialize maze
    for y in range(2):
        for x in range(2):
            maze[y][x] = calculate_space(x, y)

    locations = set()
    count_locations([(1, 1)], maze, locations)

    print('Part 2: {}'.format(len(locations)))

part_1()
part_2()
