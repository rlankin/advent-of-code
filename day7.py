import re

instructions = {}

# Read file
inst_regex = re.compile("(.*) -> (.*)")
with open('input/day7_input.txt', 'r') as f:
    for inst in f:
        i = inst.split(" -> ")
        lhs = i[0].split(" ")

        if len(lhs) == 1:
            instructions[i[1].rstrip()] = (lhs[0])
        elif len(lhs) == 2:
            instructions[i[1].rstrip()] = (lhs[0], lhs[1])
        elif len(lhs) == 3:
            instructions[i[1].rstrip()] = (lhs[1], lhs[0], lhs[2])

def evaluate(wire):
    value = 0

    try:
        value = int(wire)
    except ValueError:
        inst = instructions[wire]
        if str(type(inst)) != "<class 'tuple'>":
            value = evaluate(inst)
        elif len(inst) == 2:
            # The only unary operation is NOT
            value = ~evaluate(inst[1])
        elif len(inst) == 3:
            if inst[0] == "AND":
                value = evaluate(inst[1]) & evaluate(inst[2])
            elif inst[0] == "OR":
                value = evaluate(inst[1]) | evaluate(inst[2])
            elif inst[0] == "LSHIFT":
                value = evaluate(inst[1]) << int(inst[2])
            elif inst[0] == "RSHIFT":
                value = evaluate(inst[1]) >> int(inst[2])

    value &= 0xffff
    instructions[wire] = value

    return value

def part_1():
    print("Part 1: " + str(evaluate("a")))

def part_2():
    """Wire b is manually set to the answer from part 1 because I'm too lazy to
    structure the program properly. This also means that the print outs for
    parts 1 and 2 cannot be run at the same time.
    """
    instructions["b"] = 46065
    print("Part 2: " + str(evaluate("a")))

#part_1()
part_2()
