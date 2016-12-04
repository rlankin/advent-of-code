import re

def is_real_room(name, checksum):
    hist = {}
    for letter in name.replace('-', ''):
        hist[letter] = hist[letter] + 1 if letter in hist else 1

    sorted_hist = [(k, hist[k]) for k in sorted(hist, key=hist.get, reverse=True)]

    sort_complete = False
    while not sort_complete:
        sort_complete = True

        for i in range(0, len(sorted_hist) - 1):
            if sorted_hist[i][1] == sorted_hist[i + 1][1] \
                    and sorted_hist[i][0] > sorted_hist[i + 1][0]:
                sorted_hist[i], sorted_hist[i + 1] = sorted_hist[i + 1], sorted_hist[i]
                sort_complete = False

    return ''.join([letter[0] for letter in sorted_hist])[:5] == checksum

def rotate_letter(letter, rotations):
    int_letter = ord(letter) - 97
    int_letter = (int_letter + rotations) % 26
    return chr(int_letter + 97)

def part_1():
    sector_id_sum = 0

    with open('input/day4_input.txt', 'r') as f:
        for line in f:
            match = re.search('([a-z\-]+)-([0-9]+)\[([a-z]+)\]', line)
            if match is not None:
                name = match.group(1)
                sector_id = int(match.group(2))
                checksum = match.group(3)

                if is_real_room(name, checksum):
                    sector_id_sum = sector_id_sum + sector_id
            else:
                print('No match found for {}'.format(example))

    print('Part 1: {}'.format(sector_id_sum))

def part_2():
    with open('input/day4_input.txt', 'r') as f:
        for line in f:
            match = re.search('([a-z\-]+)-([0-9]+)\[([a-z]+)\]', line)
            if match is not None:
                name = match.group(1)
                sector_id = int(match.group(2))
                checksum = match.group(3)

                if is_real_room(name, checksum):
                    decrypted_chars = []
                    for c in name:
                        if c == '-':
                            decrypted_chars.append(' ')
                        else:
                            decrypted_chars.append(rotate_letter(c, sector_id))

                    print('{}: {}'.format(sector_id, ''.join(decrypted_chars)))
            else:
                print('No match found for {}'.format(example))

part_1()
part_2()
