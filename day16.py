import re

mfcsam = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

sues = []

# Read Sue information from day16_input.py
sue_re = re.compile("Sue ([0-9]+): (.*): ([0-9]+), (.*): ([0-9]+), (.*): ([0-9]+)")
with open("input/day16_input.txt") as f:
    for sue in f:
        m = sue_re.match(sue)
        if m:
            sues.append({m.group(2): int(m.group(3)), m.group(4): int(m.group(5)), m.group(6): int(m.group(7))})

def part_1():
    potential_sues = []

    for num, sue in enumerate(sues):
        potential = True
        for k, v in sue.items():
            if mfcsam[k] != v:
                potential = False
                break

        if potential:
            potential_sues.append(num + 1)

    print("Part 1: " + str(potential_sues))

def part_2():
    potential_sues = []

    for num, sue in enumerate(sues):
        potential = True
        for k, v in sue.items():
            if k == "cats" or k == "trees":
                if v <= mfcsam[k]:
                    potential = False
                    break
            if k == "pomeranians" or k == "goldfish":
                if v >= mfcsam[k]:
                    potential = False
                    break
            else:
                if mfcsam[k] != v:
                    potential = False
                    break

        if potential:
            potential_sues.append(num + 1)

    print("Part 2: " + str(potential_sues))

part_1()
part_2()
