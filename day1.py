def part_1():
    floor = 0

    with open('input/day1_input.txt', 'r') as f:
        while True:
            direction = f.read(1)
            if not direction:
                break

            floor += 1 if direction == "(" else -1

    return floor

def part_2():
    floor = 0
    count = 0

    with open('input/day1_input.txt', 'r') as f:
        while True:
            direction = f.read(1)
            if not direction:
                break

            count += 1
            floor += 1 if direction == "(" else -1

            if floor == -1:
                break

    return count

print("(Part 1) Final floor: " + str(part_1()))
print("(Part 2) Position of first basement move: " + str(part_2()))
