from itertools import groupby

INVALID_CHARACTERS = (ord("i"), ord("l"), ord("o"))

def is_run(c):
    return c[1] == c[2] - 1 and c[0] == c[2] - 2

def is_valid(password):
    # Passwords cannot contain "i", "l", or "o"
    all_valid_chars = not any(c in password for c in INVALID_CHARACTERS)

    # Check for double letters (need at least 2 non-overlapping pairs)
    two_pairs = len([k for (k, g) in groupby(password) if len(list(g)) > 1]) > 1

    # Detect consecutive runs of characters ("abc", "xyz", etc)
    run_found = any([True for c in range(2, len(password)) if is_run(password[c - 2:c + 1])])

    '''
    if password == [ord("a"), ord("b"), ord("c"), ord("d"), ord("f"), ord("f"), ord("a"), ord("a")]:
        print("{0} {1} {2}".format(all_valid_chars, two_pairs, run_found))
    '''

    return all_valid_chars and two_pairs and run_found

def increment(password):
    new_password = password

    for i in range(len(new_password), 0, -1):
        if new_password[i - 1] == ord("z") + 1:
            new_password[i - 1] = 97

        new_password[i - 1] += 1

        if new_password[i - 1] == ord("z") + 1:
            new_password[i - 1] = 97
        elif new_password[i - 1] in INVALID_CHARACTERS:
            new_password[i - 1] += 1
            break
        else:
            break

    return new_password

def get_next_password(password):
    p_list = [ord(c) for c in password]
    p_list = increment(p_list)

    # Pre-process string to remove any invalid characters
    invalid_found = False
    for i in range(len(p_list)):
        if invalid_found:
            p_list[i] = ord("a")
        elif p_list[i] in INVALID_CHARACTERS:
            p_list[i] += 1
            invalid_found = True

    while not is_valid(p_list):
        p_list = increment(p_list)

    return "".join([chr(c) for c in p_list])

def part_1():
    print("Part 1: " + get_next_password("hepxcrrq"))

def part_2():
    print("Part 2: " + get_next_password("hepxxyzz"))

part_1()
part_2()
