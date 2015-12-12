vowels = ["a", "e", "i", "o", "u"]

def part_1():
    nice_count = 0

    with open('input/day5_input.txt', 'r') as f:
        for s in f:
            v_count = 0
            double_let = False
            naughty_seq = False

            for i, c in enumerate(s):
                # Count the vowels
                if c in vowels:
                    v_count += 1

                if i > 0:
                    # Look for naughty sequences
                    if c in ["b", "d", "q", "y"] and ord(s[i - 1]) == ord(c) - 1:
                        naughty_seq = True
                        break

                    # Look for double letters
                    if c == s[i - 1]:
                        double_let = True

            if not naughty_seq and double_let and v_count >= 3:
                nice_count += 1

    return nice_count

def part_2():
    nice_count = 0

    with open('input/day5_input.txt', 'r') as f:
        for s in f:
            repeat_let = False
            repeat_pair = False

            for i, c in enumerate(s):
                # Check for recurring pair
                if i < len(s) - 1 and s[i:i + 2] in s[i + 2:]:
                    repeat_pair = True

                if i > 1:
                    # Check for repeated letters separated by one
                    if c == s[i - 2]:
                        repeat_let = True

                if repeat_pair and repeat_let:
                    nice_count += 1
                    break

    return nice_count

print("Nice strings (part 1): " + str(part_1()))
print("Nice strings (part 2): " + str(part_2()))
