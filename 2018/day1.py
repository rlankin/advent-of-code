def part_1():
    with open('input/day1_input') as f:
        print('Part 1: {}'.format(sum(int(i) for i in f.readlines())))

def part_2():
    freq_delta = []
    with open('input/day1_input') as f:
        freq_delta = list(int(i) for i in f.readlines())
    freq = 0
    freqs = [freq]
    found = False
    while not found:
        for d in freq_delta:
            freq += d
            if freq in freqs:
                found = True
                break
            freqs.append(freq)
    print('Part 2: {}'.format(freq))

part_1()
part_2()
