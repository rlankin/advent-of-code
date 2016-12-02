"""
Puzzle input:
To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029.
"""

def get_code(row, col):
    code = 20151125
    r = 2

    while True:
        r_i = r
        c_i = 1

        while r_i > 0:
            code = (code * 252533) % 33554393

            if r_i == row and c_i == col:
                return code

            r_i -= 1
            c_i += 1

        r += 1

def part_1():
    code = get_code(2947, 3029)
    print("Part 1: " + str(code))

part_1()
