stream = ''
with open('input/day9_input', 'r') as f:
    stream = f.readline()

score = 0
group_level = 0
garbage_chars = 0

i = 0
while i < len(stream):
    if stream[i] == '<':
        while i < len(stream):
            i += 1
            if stream[i] == '!':
                i += 1
            elif stream[i] == '>':
                break
            else:
                garbage_chars += 1
    elif stream[i] == '{':
        group_level += 1
    elif stream[i] == '}':
        score += group_level
        group_level -= 1

    i += 1

print('Part 1: {}'.format(score))
print('Part 2: {}'.format(garbage_chars))
