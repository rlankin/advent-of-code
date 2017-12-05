def is_valid(passphrase, anagrams):
    words = []
    for word in passphrase.split(' '):
        if anagrams:
            for w in words:
                if all(word.count(c) == w.count(c) and len(word) == len(w) for c in word):
                    return False
        elif word in words:
            return False

        words.append(word)
    return True

def part_1():
    valid = 0
    with open('input/day4_input', 'r') as f:
        valid = sum(1 for p in f if is_valid(p.rstrip(), False))
    print('Part 1: {}'.format(valid))

def part_2():
    valid = 0
    with open('input/day4_input', 'r') as f:
        valid = sum(1 for p in f if is_valid(p.rstrip(), True))
    print('Part 2: {}'.format(valid))

part_1()
part_2()
