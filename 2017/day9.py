stream = ''
with open('input/day9_input', 'r') as f:
    stream = f.readline()

score = 0
group_level = 0
garbage_chars = 0
garbage = False
ignore = False

for c in stream:
    if ignore:
        ignore = False
        continue

    if c == '!':
        garbage_chars -= 1
        ignore = True
    elif c == '<':
        if not garbage:
            garbage_chars -= 1
        garbage = True
    elif c == '>':
        garbage = False

    if garbage:
        garbage_chars += 1
        continue

    if c == '{':
        group_level += 1
    elif c == '}':
        score += group_level
        group_level -= 1

print('Part 1: {}'.format(score))
print('Part 2: {}'.format(garbage_chars))
