INSTRUCTIONS = []

with open("input/day23_input.txt") as f:
    for row in f:
        parsed = row.rstrip().split(" ")

        if parsed[0] == "jie" or parsed[0] == "jio":
            INSTRUCTIONS.append((parsed[0], parsed[1][:-1], int(parsed[2])))
        elif parsed[0] == "jmp":
            INSTRUCTIONS.append((parsed[0], int(parsed[1])))
        else:
            INSTRUCTIONS.append((parsed[0], parsed[1]))

def run(a, b):
    r = {"a": a, "b": b}
    ic = 0

    while -1 < ic < len(INSTRUCTIONS):
        inst = INSTRUCTIONS[ic]

        if inst[0] == "hlf":
            r[inst[1]] /= 2
        if inst[0] == "tpl":
            r[inst[1]] *= 3
        if inst[0] == "inc":
            r[inst[1]] += 1
        if inst[0] == "jmp":
            ic += inst[1]
            continue
        if inst[0] == "jie":
            if r[inst[1]] % 2 == 0:
                ic += inst[2]
                continue
        if inst[0] == "jio":
            if r[inst[1]] == 1:
                ic += inst[2]
                continue

        ic += 1

    return r

def part_1():
    r = run(0, 0)
    print("Part 1: " + str(r["b"]))

def part_2():
    r = run(1, 0)
    print("Part 1: " + str(r["b"]))

part_1()
part_2()
