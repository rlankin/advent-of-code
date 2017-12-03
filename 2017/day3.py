def traverse_shell(s, target):
    l = (s * 2) + 1
    square = l ** 2
    coords = [s, -s]

    if square == target:
        return coords

    # Left
    for i in range(1, l):
        coords[0] -= 1
        square -= 1
        if square == target:
            return coords
    # Up
    for i in range(1, l):
        coords[1] += 1
        square -= 1
        if square == target:
            return coords
    # Right
    for i in range(1, l):
        coords[0] += 1
        square -= 1
        if square == target:
            return coords
    # Down
    for i in range(1, l):
        coords[1] -= 1
        square -= 1
        if square == target:
            return coords

def part_1():
    square = 277678

    # Find "shell" that the square lies in
    s = 0
    while square > ((s * 2) + 1) ** 2:
        s += 1

    coords = traverse_shell(s, square)

    print('Part 1: {}'.format(abs(coords[0]) + abs(coords[1])))

def calc_grid_value(pos, grid):
    value = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                adj = (pos[0] + x, pos[1] + y)
                if adj in grid:
                    value += grid[adj]
    return value

def find_larger(target):
    grid = { (0, 0): 1 }
    pos = [0, 0]
    l = 1

    while True:
        l += 2
        pos[0] += 1
        value = calc_grid_value(pos, grid)
        if value > target:
            return value
        grid[tuple(pos)] = value

        # Up
        for i in range(1, l - 1):
            pos[1] += 1
            value = calc_grid_value(pos, grid)
            if value > target:
                return value
            grid[tuple(pos)] = value
        # Left
        for i in range(1, l):
            pos[0] -= 1
            value = calc_grid_value(pos, grid)
            if value > target:
                return value
            grid[tuple(pos)] = value
        # Down
        for i in range(1, l):
            pos[1] -= 1
            value = calc_grid_value(pos, grid)
            if value > target:
                return value
            grid[tuple(pos)] = value
        # Right
        for i in range(1, l):
            pos[0] += 1
            value = calc_grid_value(pos, grid)
            if value > target:
                return value
            grid[tuple(pos)] = value

def part_2():
    print('Part 2: {}'.format(find_larger(277678)))

part_1()
part_2()
