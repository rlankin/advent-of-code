import hashlib

PASSCODE = 'vwbaicqe'
OPEN_VALUES = ['b', 'c', 'd', 'e', 'f']
DESTINATION = [3, 3]

def get_open_doors(passcode, path):
    open_doors = []
    values = hashlib.md5((passcode + path).encode('utf-8')).hexdigest()

    if values[0] in OPEN_VALUES:
        open_doors += 'U'
    if values[1] in OPEN_VALUES:
        open_doors += 'D'
    if values[2] in OPEN_VALUES:
        open_doors += 'L'
    if values[3] in OPEN_VALUES:
        open_doors += 'R'

    return open_doors

def get_paths(x, y, path):
    if [x, y] == DESTINATION:
        return [path]

    paths = []
    for door in get_open_doors(PASSCODE, path):
        if door == 'U' and y - 1 >= 0:
            paths += get_paths(x, y - 1, path + door)
        if door == 'D' and y + 1 < 4:
            paths += get_paths(x, y + 1, path + door)
        if door == 'L' and x - 1 >= 0:
            paths += get_paths(x - 1, y, path + door)
        if door == 'R' and x + 1 < 4:
            paths += get_paths(x + 1, y, path + door)

    return paths

def part_1():
    paths = get_paths(0, 0, '')
    print('Part 1: {}'.format(min(paths, key = len)))

def part_2():
    paths = get_paths(0, 0, '')
    print('Part 2: {}'.format(len(max(paths, key = len))))

part_1()
part_2()
