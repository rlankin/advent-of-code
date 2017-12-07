def redistribute(banks):
    max_bank = max(enumerate(banks), key=lambda b: b[1])
    banks[max_bank[0]] = 0
    for i in range(max_bank[0] + 1, max_bank[0] + 1 + max_bank[1]):
        banks[i % len(banks)] += 1

banks = []
history = []
count = 0

with open('input/day6_input', 'r') as f:
    banks = [int(b) for b in f.read().split('\t')]

history.append(list(banks))
while banks not in history[:-1]:
    redistribute(banks)
    history.append(list(banks))
    count += 1

print('Part 1: {}'.format(count))
print('Part 2: {}'.format(len(history) - 1 - history.index(history[-1])))
