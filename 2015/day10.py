from itertools import groupby

input_string = "1321131112"

def part_1():
    lns = input_string
    for i in range(40):
        lns_next = ""
        for k, g in groupby(lns):
            numbers = list(g)
            lns_next += str(len(numbers)) + k

        lns = lns_next

    print("Part 1: {0}".format(len(lns)))

def part_2():
    lns = input_string
    for i in range(50):
        lns_next = ""
        for k, g in groupby(lns):
            numbers = list(g)
            lns_next += str(len(numbers)) + k

        lns = lns_next

    print("Part 2: {0}".format(len(lns)))

part_1()
part_2()
