def advance_scanner(s):
    if s[1] == s[0] - 1:
        s[2] = -1
    elif s[1] == 0:
        s[2] = 1
    s[1] += s[2]

# layers = {0: [3, 0, 1], 1: [2, 0, 1], 4: [4, 0, 1], 6: [4, 0, 1]}
layers = {}
with open('input/day13_input', 'r') as f:
    for line in f:
        layer = line.split(':')
        layers[int(layer[0])] = [int(layer[1]), 0, 1]

pos = -1
severity = 0
for t in range(max(layers) + 1):
    pos += 1
    for d, s in layers.items():
        if pos == d and s[1] == 0:
            severity += d * s[0]
        advance_scanner(s)

print('Part 1: {}'.format(severity))

delay = -1
through = False
while not through:
    for d, s in layers.items():
        s[1] = 0
        s[2] = 1

    pos = -1
    delay += 1
    for t in range(delay):
        for d, s in layers.items():
            advance_scanner(s)

    through = True
    for t in range(max(layers) + 1):
        pos += 1
        for d, s in layers.items():
            if pos == d and s[1] == 0:
                through = False
                break
            advance_scanner(s)
        if not through:
            break

print('Part 2: {}'.format(delay))
