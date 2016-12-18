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

def count_safe_tiles(total_rows):
    room = [FIRST_ROW]
    safe_tiles = room[-1].count('.')

    for i in range(total_rows - 1):
        room.append(get_next_row(room[-1]))
        safe_tiles += room[-1].count('.')

    return safe_tiles

def part_1():
    print('Part 1: {}'.format(count_safe_tiles(40)))

def part_2():
    print('Part 2: {}'.format(count_safe_tiles(400000)))

part_1()
part_2()
