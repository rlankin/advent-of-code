import hashlib

key = b"bgvyzdsv"

def part_1():
    n = 1
    while True:
        m = hashlib.md5()
        m.update(key + str(n).encode())
        digest = m.hexdigest()
        if digest[:5] == "00000":
            return n
        n += 1

def part_2():
    n = 1
    while True:
        m = hashlib.md5()
        m.update(key + str(n).encode())
        digest = m.hexdigest()
        if digest[:6] == "000000":
            return n
        n += 1

print("Lowest valid number ('00000'): " + str(part_1()))
print("Lowest valid number ('000000'): " + str(part_2()))
