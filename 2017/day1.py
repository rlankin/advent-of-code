def part_1():
    with open('input/day1_input', 'r') as f:
        captcha = f.read().strip()
        s = sum([int(x) for i, x in enumerate(captcha) if x == captcha[(i + 1) % len(captcha)]])
        print('Part 1: {}'.format(s))

def part_2():
    with open('input/day1_input', 'r') as f:
        captcha = f.read().strip()
        h = int(len(captcha) / 2)
        s = sum([int(x) for i, x in enumerate(captcha) if x == captcha[(i + h) % len(captcha)]])
        print('Part 2: {}'.format(s))

part_1()
part_2()
