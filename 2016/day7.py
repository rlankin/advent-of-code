import re

ABBA_RE = re.compile('(.)(.)\\2\\1')
ABA_RE = re.compile('(?=(.)(.)\\1)')

def parse_ip(ip):
    sequences = [[], []] # supernet, hypernet
    sequence = ''

    for c in ip:
        if c == ']':
            sequences[1].append(sequence)
            sequence = ''
        elif c == '[':
            if sequence != '':
                sequences[0].append(sequence)
                sequence = ''
        else:
            sequence = sequence + c

    if sequence != '':
        sequences[0].append(sequence)

    return sequences

def contains_ABBA(sequence):
    match = ABBA_RE.search(sequence)
    return match is not None and match.group(1) != match.group(2)

def contains_ABA_BAB(ip):
    parsed = parse_ip(ip)

    for supernet in parsed[0]:
        for match in ABA_RE.findall(supernet):
            a = match[0]
            b = match[1]

            if a != b and \
                any([re.search('{}{}{}'.format(b, a, b), hypernet) for hypernet in parsed[1]]):
                return True

    return False

def part_1():
    support_TLS = 0

    with open('input/day7_input.txt', 'r') as f:
        for ip in f:
            parsed = parse_ip(ip.strip())

            if all(not contains_ABBA(s) for s in parsed[1]) \
                and any(contains_ABBA(s) for s in parsed[0]):
                support_TLS = support_TLS + 1

    print('Part 1: {}'.format(support_TLS))

def part_2():
    support_SSL = 0

    with open('input/day7_input.txt', 'r') as f:
        for ip in f:
            if contains_ABA_BAB(ip.strip()):
                support_SSL = support_SSL + 1

    print('Part 2: {}'.format(support_SSL))

part_1()
part_2()
