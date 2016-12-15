import hashlib
import re

SALT = 'ahsbgdzn'
TRIPLE_RE = re.compile('(.)\\1\\1')

def part_1():
    keys = []
    stream = []

    index = 0
    while len(keys) < 64:
        h = hashlib.md5((SALT + str(index)).encode('utf-8')).hexdigest()

        for p in stream:
            if p[1] and p[1] * 5 in h:
                keys.append(p)
                p[1] = None

        match = TRIPLE_RE.search(h)
        stream.append([index, match.group(1) if match else None, h])

        if len(stream) > 1000:
            stream.pop(0)

        index += 1

    # Sort keys and truncate because they may have gotten added out of order
    keys = (sorted(keys, key = lambda k: k[0]))[:64]

    print('Part 1: {}'.format(keys[-1][0]))

def part_2():
    keys = []
    stream = []

    index = 0
    while len(keys) < 64:
        h = SALT + str(index)
        for i in range(2017):
            h = hashlib.md5(h.encode('utf-8')).hexdigest()

        for p in stream:
            if p[1] and p[1] * 5 in h:
                keys.append(p)
                p[1] = None

        match = TRIPLE_RE.search(h)
        stream.append([index, match.group(1) if match else None, h])

        if len(stream) > 1000:
            stream.pop(0)

        index += 1

    # Sort keys and truncate because they may have gotten added out of order
    keys = (sorted(keys, key = lambda k: k[0]))[:64]

    print('Part 2: {}'.format(keys[-1][0]))

part_1()
part_2()
