import hashlib

key = b"bgvyzdsv"

def part_1():
    n = 1
    while True:
        m = hashlib.md5()
        m.update(key + str(n).encode())
        digest = m.hexdigest()
        if digest[:5] == "00000":
            break
        n += 1

    print("Part 1: " + str(n))

def part_2():
    n = 1
    while True:
        m = hashlib.md5()
        m.update(key + str(n).encode())
        digest = m.hexdigest()
        if digest[:6] == "000000":
            break
        n += 1

    print("Part 2: " + str(n))

part_1()
part_2()
