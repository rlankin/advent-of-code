FIRST_ROW = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'

def get_tile(left, center, right):
    is_trap = (left == '^' and center == '^' and right == '.') \
        or (left == '.' and center == '^' and right == '^') \
        or (left == '^' and center == '.' and right == '.') \
        or (left == '.' and center == '.' and right == '^')
    return '^' if is_trap else '.'

def get_next_row(row):
    next_row = ''

    for i in range(len(row)):
        next_row += get_tile(row[i - 1] if i > 0 else '.', row[i], row[i + 1] if i < len(row) - 1 else '.')

    return next_row

def part_1():
    room = [FIRST_ROW]
    safe_tiles = sum([1 for tile in room[0] if tile == '.'])

    for i in range(39):
        room.append(get_next_row(room[-1]))
        safe_tiles += sum([1 for tile in room[-1] if tile == '.'])

    print('Part 1: {}'.format(safe_tiles))

def part_2():
    room = [FIRST_ROW]
    safe_tiles = sum([1 for tile in room[0] if tile == '.'])

    for i in range(399999):
        room.append(get_next_row(room[-1]))
        safe_tiles += sum([1 for tile in room[-1] if tile == '.'])

    print('Part 2: {}'.format(safe_tiles))

part_1()
part_2()
