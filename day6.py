import re

inst_regex = re.compile("(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

def parse_instruction(i):
    p = inst_regex.match(i)
    return [p.group(1), (int(p.group(2)), int(p.group(3))), (int(p.group(4)), int(p.group(5)))]

def part_1():
    lights = set()

    with open('input/day6_input.txt', 'r') as f:
        for i in f:
            inst = parse_instruction(i)
            l_temp = set()
            for x in range(inst[1][0], inst[2][0] + 1):
                for y in range(inst[1][1], inst[2][1] + 1):
                    l_temp.add((x, y))

            if inst[0] == "turn on":
                lights |= l_temp
            elif inst[0] == "turn off":
                lights -= l_temp
            elif inst[0] == "toggle":
                lights ^= l_temp

    print("Part 1: " + str(len(lights)))

def part_2():
    lights = [[0 for j in range(1000)] for i in range(1000)]

    with open('input/day6_input.txt', 'r') as f:
        for i in f:
            inst = parse_instruction(i)
            for x in range(inst[1][0], inst[2][0] + 1):
                for y in range(inst[1][1], inst[2][1] + 1):
                    if inst[0] == "turn on":
                        lights[x][y] += 1
                    elif inst[0] == "turn off" and lights[x][y] > 0:
                        lights[x][y] -= 1
                    elif inst[0] == "toggle":
                        lights[x][y] += 2

    brightness = sum([sum(row) for row in lights])

    print("Part 2: " + str(brightness))

part_1()
part_2()
