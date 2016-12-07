def get_char_hists():
    char_hists = []

    with open('input/day6_input.txt', 'r') as f:
        for message in f:
            m = message.strip()

            if len(char_hists) == 0:
                char_hists = [dict() for c in m]

            for i, c in enumerate(m):
                char_hists[i][c] = char_hists[i][c] + 1 if c in char_hists[i] else 1

    return char_hists

def part_1():
    char_hists = get_char_hists()
    corrected_message = ''.join([max(hist, key = hist.get) for hist in char_hists])
    print('Part 1: {}'.format(corrected_message))

def part_2():
    char_hists = get_char_hists()
    corrected_message = ''.join([min(hist, key = hist.get) for hist in char_hists])
    print('Part 2: {}'.format(corrected_message))

part_1()
part_2()
