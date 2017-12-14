from functools import reduce

def knot_hash_round(lst, lengths, pos, skip):
    for l in lengths:
        rev = list(reversed([lst[(pos + i) % len(lst)] for i in range(l)]))
        for i in range(l):
            lst[(pos + i) % len(lst)] = rev[i]
        pos += (l + skip) % len(lst)
        skip += 1
    return pos, skip

def knot_hash(value):
    lengths = [ord(c) for c in value] + [17, 31, 73, 47, 23]
    lst = [i for i in range(256)]
    pos = 0
    skip = 0
    for r in range(64):
        pos, skip = knot_hash_round(lst, lengths, pos, skip)
    dense_hash = [reduce(lambda x, y: x ^ y, lst[i*16:(i+1)*16]) for i in range(16)]
    return ''.join(format(i, '02x') for i in dense_hash)

def adjacent(s, x, y):
    return ((abs(s[0] - x) <= 1 and s[1] == y)
            or (s[0] == x and abs(s[1] - y) <= 1))

key_str = 'wenycdww'
used = 0
regions = []
for r in range(128):
    kh = knot_hash('{}-{}'.format(key_str, r))
    kh_bin = bin(int(kh, 16))[2:].zfill(128)
    for c in range(len(kh_bin)):
        if kh_bin[c] == '1':
            used += 1
            matches = []
            for region in regions:
                if any(adjacent(s, c, r) for s in region):
                    matches.append(region)
            if matches:
                new_region = [[c, r]]
                for match in matches:
                    regions.remove(match)
                    new_region += match
                regions.append(new_region)
            else:
                regions.append([[c, r]])

print('Part 1: {}'.format(used))
print('Part 2: {}'.format(len(regions)))
