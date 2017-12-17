import math

def dance_move(programs, move):
    if move[0] == 's':
        programs = programs[-move[1]:] + programs[:-move[1]]
    elif move[0] == 'x':
        temp = programs[move[1]]
        programs[move[1]] = programs[move[2]]
        programs[move[2]] = temp
    elif move[0] == 'p':
        temp = programs.index(move[1])
        programs[programs.index(move[2])] = move[1]
        programs[temp] = move[2]
    return programs

def dance(programs, moves, iterations):
    starting = list(programs)
    i = 0
    while i < iterations:
        for move in moves:
            programs = dance_move(programs, move)
        if programs == starting:
            i += (math.floor(iterations / (i + 1)) - 1) * (i + 1)
        i += 1
    return programs

moves = []
with open('input/day16_input', 'r') as f:
    for m in f.readline().strip().split(','):
        if m[0] == 's':
            moves.append([m[0], int(m[1:])])
        elif m[0] == 'x':
            i = m[1:].split('/')
            moves.append([m[0], int(i[0]), int(i[1])])
        elif m[0] == 'p':
            p = m[1:].split('/')
            moves.append([m[0], p[0], p[1]])

print('Part 1: {}'.format(''.join(dance([c for c in 'abcdefghijklmnop'], moves, 1))))
print('Part 2: {}'.format(''.join(dance([c for c in 'abcdefghijklmnop'], moves, 1000000000))))
