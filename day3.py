def part_1():
    houses = set()
    houses.add((0, 0))

    with open('input/day3_input.txt', 'r') as f:
        loc = [0, 0]

        while True:
            direction = f.read(1)
            if not direction:
                break

            if direction == "^":
                loc[1] += 1
            elif direction == ">":
                loc[0] += 1
            elif direction == "v":
                loc[1] -= 1
            elif direction == "<":
                loc[0] -= 1

            houses.add((loc[0], loc[1]))

    return len(houses)

def part_2():
    houses = set()
    houses.add((0, 0))

    with open('input/day3_input.txt', 'r') as f:
        loc_s = [0, 0]
        loc_rs = [0, 0]
        s_move = True

        while True:
            direction = f.read(1)
            if not direction:
                break

            loc = loc_s if s_move else loc_rs

            if direction == "^":
                loc[1] += 1
            elif direction == ">":
                loc[0] += 1
            elif direction == "v":
                loc[1] -= 1
            elif direction == "<":
                loc[0] -= 1

            houses.add((loc[0], loc[1]))

            s_move = not s_move

    return len(houses)

print("Houses visited (Santa): " + str(part_1()))
print("Houses visited (Santa + Robo-Santa): " + str(part_2()))
