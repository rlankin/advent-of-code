def part_1():
    total = 0

    with open('input/day2_input.txt', 'r') as f:
        for dim_text in f:
            dim = sorted([int(d) for d in dim_text.rstrip().split("x")])

            # Surface area = 2lw + 2wh + 2hl = 2(lw + wh + hl)
            total += 2 * ((dim[0] * dim[1]) + (dim[1] * dim[2]) + (dim[2] * dim[0]))

            # Add in extra slack (area of smallest side)
            total += dim[0] * dim[1]

    return total

def part_2():
    total = 0

    with open('input/day2_input.txt', 'r') as f:
        for dim_text in f:
            dim = sorted([int(d) for d in dim_text.rstrip().split("x")])

            # Shortest sides are first, since the dimensions are sorted
            total += (2 * dim[0]) + (2 * dim[1])

            # Add in amount for bow
            total += dim[0] * dim[1] * dim[2]

    return total

print("(Part 1) Total paper: " + str(part_1()) + " sq ft")
print("(Part 2) Total ribbon: " + str(part_2()) + " ft")
