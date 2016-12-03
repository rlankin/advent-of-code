def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def part_1():
    valid_triangles = 0

    with open('input/day3_input.txt', 'r') as f:
        for line in f:
            sides = line.split()
            if (is_triangle(int(sides[0]), int(sides[1]), int(sides[2]))):
                valid_triangles = valid_triangles + 1

    print('Part 1: {}'.format(valid_triangles))

def part_2():
    valid_triangles = 0

    with open('input/day3_input.txt', 'r') as f:
        line1 = f.readline()
        while line1 != '':
            sides1 = [int(s) for s in line1.split()]
            sides2 = [int(s) for s in f.readline().split()]
            sides3 = [int(s) for s in f.readline().split()]

            for i in range(0, 3):
                if (is_triangle(sides1[i], sides2[i], sides3[i])):
                    valid_triangles = valid_triangles + 1

            line1 = f.readline()

    print('Part 2: {}'.format(valid_triangles))

part_1()
part_2()
