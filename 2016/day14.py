import hashlib
import re

SALT = 'ahsbgdzn'
TRIPLE_RE = re.compile('(.)\\1\\1')

def generate_keys(num_keys, salt, hash_function):
    keys = []
    stream = []

    index = 0
    while len(keys) < num_keys:
        h = hash_function(salt, index)

        # Look for potential keys that have not yet been approved and whose
        # second condition is satisfied by this new hash
        for p in stream:
            if p[1] and p[1] * 5 in h:
                keys.append(p)
                p[1] = None # Indicate that this key has been approved

        match = TRIPLE_RE.search(h)
        # Key format: (index, repeated character, hash)
        stream.append([index, match.group(1) if match else None, h])

        # Roll the oldest key off the stream; it's either been found or is not
        # valid
        if len(stream) > 1000:
            stream.pop(0)

        index += 1

    # Sort and truncate keys, as they may have been added out of order and more
    # may have been added than were requested
    return (sorted(keys, key = lambda k: k[0]))[:num_keys]

def standard_hash(salt, index):
    return hashlib.md5((salt + str(index)).encode('utf-8')).hexdigest()

def stretched_hash(salt, index):
    h = salt + str(index)
    for i in range(2017):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()

    return h

def part_1():
    keys = generate_keys(64, SALT, standard_hash)
    print('Part 1: {}'.format(keys[-1][0]))

def part_2():
    keys = generate_keys(64, SALT, stretched_hash)
    print('Part 2: {}'.format(keys[-1][0]))

part_1()
part_2()
