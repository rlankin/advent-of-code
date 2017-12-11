def cube_move(d, pos):
    if d == 'n':
        pos[1] += 1
        pos[2] -= 1
    elif d == 'ne':
        pos[0] += 1
        pos[2] -= 1
    elif d == 'se':
        pos[0] += 1
        pos[1] -= 1
    elif d == 's':
        pos[1] -= 1
        pos[2] += 1
    elif d == 'sw':
        pos[0] -= 1
        pos[2] += 1
    elif d == 'nw':
        pos[0] -= 1
        pos[1] += 1

def cube_dist(a, b):
    return max(abs(a[i] - b[i]) for i in range(len(a)))

path = []
with open('input/day11_input', 'r') as f:
    path = f.readline().strip().split(',')

pos = [0, 0, 0]
max_dist = 0

for step in path:
    cube_move(step, pos)
    dist = cube_dist([0, 0, 0], pos)
    if dist > max_dist:
        max_dist = dist

print('Part 1: {}'.format(cube_dist([0, 0, 0], pos)))
print('Part 2: {}'.format(max_dist))
