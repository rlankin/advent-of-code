lights = []
with open("input/day18_input.txt") as f:
    for row in f:
        lights.append(list(row.rstrip()))

GRID_SIZE = len(lights[0])

def print_lights(lights):
    print("--------------------")
    for row in lights:
        print(row)
    print("--------------------")

def count_neighbors(lights, r, c):
    """
    Let A = lights[r][c].
    1 2 3
    8 A 4
    7 6 5
    """
    neighbors = 0

    if r > 0 and c > 0: # 1
        neighbors += 1 if lights[r - 1][c - 1] == "#" else 0

    if r > 0: # 2
        neighbors += 1 if lights[r - 1][c] == "#" else 0

    if r > 0 and c < GRID_SIZE - 1: # 3
        neighbors += 1 if lights[r - 1][c + 1] == "#" else 0

    if c < GRID_SIZE - 1: # 4
        neighbors += 1 if lights[r][c + 1] == "#" else 0

    if r < GRID_SIZE - 1 and c < GRID_SIZE - 1: # 5
        neighbors += 1 if lights[r + 1][c + 1] == "#" else 0

    if r < GRID_SIZE - 1: # 6
        neighbors += 1 if lights[r + 1][c] == "#" else 0

    if r < GRID_SIZE - 1 and c > 0: # 7
        neighbors += 1 if lights[r + 1][c - 1] == "#" else 0

    if c > 0: # 8
        neighbors += 1 if lights[r][c - 1] == "#" else 0

    return neighbors

def step(lights):
    next_state = [row[:] for row in lights]

    for r, row in enumerate(lights):
        for c, light in enumerate(row):
            neighbors = count_neighbors(lights, r, c)

            if light == "#":
                if neighbors != 2 and neighbors != 3:
                    next_state[r][c] = "."
            else:
                if neighbors == 3:
                    next_state[r][c] = "#"

    return next_state

def part_1(lights):
    for i in range(100):
        lights = step(lights)

    lights_on = 0
    for row in lights:
        lights_on += len([l for l in row if l == "#"])

    print("Part 1: " + str(lights_on))

def part_2(lights):
    # The four corners must stay on
    lights[0][0] = "#"
    lights[0][GRID_SIZE - 1] = "#"
    lights[GRID_SIZE - 1][GRID_SIZE - 1] = "#"
    lights[GRID_SIZE - 1][0] = "#"

    for i in range(100):
        lights = step(lights)

        # The four corners must stay on
        lights[0][0] = "#"
        lights[0][GRID_SIZE - 1] = "#"
        lights[GRID_SIZE - 1][GRID_SIZE - 1] = "#"
        lights[GRID_SIZE - 1][0] = "#"

    lights_on = 0
    for row in lights:
        lights_on += len([l for l in row if l == "#"])

    print("Part 2: " + str(lights_on))

part_1(lights)
part_2(lights)
