ELVES = 5
# ELVES = 3014387

def part_1():
    """Part 1 is just the Josephus Problem:
    https://en.wikipedia.org/wiki/Josephus_problem
    https://www.youtube.com/watch?v=uCsD3ZGzMgE
    """
    l = ELVES - 2 ** (ELVES.bit_length() - 1)
    print('Part 1: {}'.format(l * 2 + 1))

part_1()
