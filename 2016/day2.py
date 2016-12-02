def part_1():
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    x = 1
    y = 1
    code = ''

    with open('input/day2_input.txt', 'r') as f:
        for line in f:
            for direction in line.rstrip():
                if direction == 'U' and y > 0:
                    y = y - 1
                elif direction == 'R' and x < 2:
                    x = x + 1
                elif direction == 'D' and y < 2:
                    y = y + 1
                elif direction == 'L' and x > 0:
                    x = x - 1

            code = code + str(keypad[y][x])

    print('Part 1: {}'.format(code))

def part_2():
    keypad = [[-1, -1, 1, -1, -1], [-1, 2, 3, 4, -1], [5, 6, 7, 8, 9], [-1, 'A', 'B', 'C', -1], [-1, -1, 'D', -1, -1]]
    x = 0
    y = 2
    code = ''

    with open('input/day2_input.txt', 'r') as f:
        for line in f:
            for direction in line.rstrip():
                if direction == 'U' and y > 0 and keypad[y - 1][x] != -1:
                    y = y - 1
                elif direction == 'R' and x < 4 and keypad[y][x + 1] != -1:
                    x = x + 1
                elif direction == 'D' and y < 4 and keypad[y + 1][x] != -1:
                    y = y + 1
                elif direction == 'L' and x > 0 and keypad[y][x - 1] != -1:
                    x = x - 1

            code = code + str(keypad[y][x])

    print('Part 2: {}'.format(code))

part_1()
part_2()
