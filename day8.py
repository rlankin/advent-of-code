def get_net_characters(s):
    mem_count = 0

    i = 1
    while i < len(s) - 1:
        if s[i] == "\\":
            if s[i + 1] == "x":
                mem_count += 1
                i += 3
            elif s[i + 1] == "\\" or s[i + 1] == "\"":
                mem_count += 1
                i += 1
        else:
            mem_count += 1

        i += 1

    return len(s) - mem_count

def part_1():
    net_characters = 0

    with open("input/day8_input.txt") as f:
        for s in f:
            net_characters += get_net_characters(s)

    return net_characters

def part_2():
    net_characters = 0

    with open("input/day8_input.txt") as f:
        for s in f:
            s_encode = "\"" + s.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
            net_characters += len(s_encode) - len(s)

    return net_characters

print("Net characters (part 1): " + str(part_1()))
print("Net characters (part 2): " + str(part_2()))
