import hashlib

DOOR_ID = 'abbhdwsy'

def part_1():
    password = ''
    index = 0

    while len(password) < 8:
        h = hashlib.md5((DOOR_ID + str(index)).encode('utf-8')).hexdigest()
        if h[:5] == '00000':
            password = password + h[5]

        index = index + 1

    print('Part 1: {}'.format(password))

def part_2():
    password = [None] * 8
    index = 0

    while None in password:
        h = hashlib.md5((DOOR_ID + str(index)).encode('utf-8')).hexdigest()
        if h[:5] == '00000' and h[5].isdigit() and int(h[5]) < 8 \
                and password[int(h[5])] is None:
            password[int(h[5])] = h[6]

        index = index + 1

    print('Part 2: {}'.format(''.join(password)))

part_1()
part_2()
