def generate_dragon_data(a):
    return a + '0' + ''.join(['1' if b == '0' else '0' for b in a[::-1]])

def calculate_checksum(data):
    checksum = ''.join(['1' if data[i] == data[i + 1] else '0' for i in range(0, len(data), 2)])
    return checksum if len(checksum) % 2 != 0 else calculate_checksum(checksum)

def part_1():
    disk_size = 272
    data = '11100010111110100'

    while len(data) < disk_size:
        data = generate_dragon_data(data)
    data = data[:disk_size]

    checksum = calculate_checksum(data)

    print('Part 1: {}'.format(checksum))

def part_2():
    disk_size = 35651584
    data = '11100010111110100'

    while len(data) < disk_size:
        data = generate_dragon_data(data)
    data = data[:disk_size]

    checksum = calculate_checksum(data)

    print('Part 2: {}'.format(checksum))

part_1()
part_2()
