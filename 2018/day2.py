from collections import defaultdict
import difflib

def part_1():
    r2, r3 = 0, 0
    with open('input/day2_input') as f:
        for box_id in f:
            counts = defaultdict(int)
            for l in box_id.strip():
                counts[l] += 1
            if 2 in counts.values():
                r2 += 1
            if 3 in counts.values():
                r3 += 1
    print('Part 1: {}'.format(r2 * r3))

def part_2():
    ids = []
    with open('input/day2_input') as f:
        ids = [i.strip() for i in f]
    for i, id1 in enumerate(ids):
        for id2 in ids[i + 1:]:
            diff = difflib.ndiff(id1, id2)
            c_diff = [c[-1] for c in diff if c[0] != ' ']
            if len(c_diff) == 2:
                print('Part 2: {}'.format(id1.replace(c_diff[0], '')))
                return

part_1()
part_2()
