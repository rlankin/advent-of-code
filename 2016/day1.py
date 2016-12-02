def get_new_heading(heading, turn):
    return (heading + (1 if turn == 'R' else -1)) % 4

def part_1():
    heading = 0
    x = 0
    y = 0
    visited = {}

    with open('input/day1_input.txt', 'r') as f:
        for step in f.read().split(', '):
            heading = get_new_heading(heading, step[0])
            distance = int(step[1:])

            if heading == 0:
                y = y + distance
            elif heading == 1:
                x = x + distance
            elif heading == 2:
                y = y - distance
            else:
                x = x - distance

    print('Part 1: {}'.format(abs(x) + abs(y)))

def part_2():
    heading = 0
    x = 0
    y = 0
    visited = []

    with open('input/day1_input.txt', 'r') as f:
        found = False

        for step in f.read().split(', '):
            heading = get_new_heading(heading, step[0])
            distance = int(step[1:])

            for i in range(0, distance):
                if heading == 0:
                    y = y + 1
                elif heading == 1:
                    x = x + 1
                elif heading == 2:
                    y = y - 1
                else:
                    x = x - 1

                if [x, y] in visited:
                    found = True
                    break
                else:
                    visited.append([x, y])

            if found:
                break

    print('Part 2: {}'.format(abs(x) + abs(y)))

part_1()
part_2()
