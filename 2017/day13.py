layers = {}
with open('input/day13_input', 'r') as f:
    for line in f:
        layer = line.split(':')
        layers[int(layer[0])] = [int(layer[1]), 0, 1]

severity = 0
for t in range(max(layers) + 1):
    if t in layers and t % ((layers[t][0] - 1) * 2) == 0:
        severity += t * layers[t][0]

print('Part 1: {}'.format(severity))

delay = -1
through = False
while not through:
    delay += 1
    pos = delay
    through = True
    for t in range(max(layers) + 1):
        if t in layers and pos % ((layers[t][0] - 1) * 2) == 0:
            through = False
            break
        pos += 1

print('Part 2: {}'.format(delay))
