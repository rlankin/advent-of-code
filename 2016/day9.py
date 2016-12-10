import re
import sys

MARKER_RE = re.compile('\(([0-9]+)x([0-9]+)\)')

def part_1():
    compressed = ''
    decompressed = ''

    with open('input/day9_input.txt', 'r') as f:
        compressed = f.read().strip()

    pos = 0
    while pos < len(compressed):
        marker = MARKER_RE.search(compressed, pos)
        if marker:
            decompressed += compressed[pos:marker.start()]

            repeated = compressed[marker.end():marker.end() + int(marker.group(1))]
            decompressed += repeated * int(marker.group(2))

            pos = marker.end() + int(marker.group(1))
        else:
            decompressed += compressed[pos:]
            break

    print('Part 1: {}'.format(len(decompressed)))

def decompressed_len(compressed):
    length = 0
    pos = 0

    while pos < len(compressed):
        marker = MARKER_RE.search(compressed, pos)
        if marker:
            length += len(compressed[pos:marker.start()])
            length += int(marker.group(2)) * decompressed_len(compressed[marker.end():marker.end() + int(marker.group(1))])

            pos = marker.end() + int(marker.group(1))
        else:
            length += len(compressed[pos:])
            break

    return length

def part_2():
    with open('input/day9_input.txt', 'r') as f:
        compressed = f.read().strip()

    print('Part 2: {}'.format(decompressed_len(compressed)))

part_1()
part_2()
