def spin_lock(step, iterations, hack=False):
    value = None
    buf = [0]
    head = 0
    for i in range(1, iterations + 1):
        head = (head + step) % i
        if hack:
            if head == 0:
                value = i
            head += 1
        else:
            head += 1
            buf.insert(head, i)
    return value if hack else buf[head + 1]

print('Part 1: {}'.format(spin_lock(316, 2017)))
print('Part 2: {}'.format(spin_lock(316, 50000000, True)))
