def find_group(programs, program, group):
    group |= {program}
    for p in programs[program]:
        if p not in group:
            find_group(programs, p, group)

programs = {}
with open('input/day12_input', 'r') as f:
    for program in f:
        p = program.strip().split('<->')
        programs[int(p[0])] = [int(pipe) for pipe in p[1].split(',')]

groups = []
for p in programs:
    if not any(p in g for g in groups):
        group = set()
        find_group(programs, p, group)
        groups.append(group)

print('Part 1: {}'.format([len(g) for g in groups if 0 in g][0]))
print('Part 2: {}'.format(len(groups)))
