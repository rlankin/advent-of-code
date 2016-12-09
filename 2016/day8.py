def draw_rect(screen, x, y):
    for r in range(y):
        screen[r][:x] = [1] * x

def rotate_row(screen, row, distance):
    for i in range(distance):
        p = screen[row].pop()
        screen[row].insert(0, p)

def rotate_column(screen, column, distance):
    for i in range(distance):
        temp = screen[-1][column]
        for r in range(len(screen)):
            temp2 = screen[r][column]
            screen[r][column] = temp
            temp = temp2

def print_screen(screen):
    for row in screen:
        print(''.join(['.' if p == 0 else '#' for p in row]))
    print()

def part_1_2():
    screen = [[0 for c in range(50)] for r in range(6)]

    with open('input/day8_input.txt', 'r') as f:
        for inst in f:
            parsed_inst = inst.strip().split()

            if parsed_inst[0] == 'rect':
                dim = parsed_inst[1].split('x')
                draw_rect(screen, int(dim[0]), int(dim[1]))
            elif parsed_inst[0] == 'rotate':
                if parsed_inst[1] == 'row':
                    rotate_row(screen, int(parsed_inst[2][2:]), int(parsed_inst[4]))
                elif parsed_inst[1] == 'column':
                    rotate_column(screen, int(parsed_inst[2][2:]), int(parsed_inst[4]))

    lit_pixels = sum([sum(column) for column in screen])

    print('Part 1: {}'.format(lit_pixels))

    print('Part 2:')
    print_screen(screen)

part_1_2()
