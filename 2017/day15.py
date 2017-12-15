MASK = 0b1111111111111111

def gen(initial, factor, div, criteria=None):
    value = initial
    while True:
        value = (value * factor) % div
        if not criteria or value % criteria == 0:
            yield value

def count_matches(gen_a, gen_b, iterations):
    matches = 0
    for i in range(iterations):
        if next(gen_a) & MASK == next(gen_b) & MASK:
            matches += 1
    return matches

matches = count_matches(gen(512, 16807, 2147483647), gen(191, 48271, 2147483647), 40000000)
print('Part 1: {}'.format(matches))

matches = count_matches(gen(512, 16807, 2147483647, 4), gen(191, 48271, 2147483647, 8), 5000000)
print('Part 2: {}'.format(matches))
