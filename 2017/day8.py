registers = {}

def get_register(name):
    if name not in registers:
        registers[name] = 0
    return registers[name]

def inc_register(name, value):
    if name not in registers:
        registers[name] = 0
    registers[name] += value

conditions = {
    '>': lambda a, b: get_register(a) > b,
    '>=': lambda a, b: get_register(a) >= b,
    '<': lambda a, b: get_register(a) < b,
    '<=': lambda a, b: get_register(a) <= b,
    '==': lambda a, b: get_register(a) == b,
    '!=': lambda a, b: get_register(a) != b
}
process_max = 0
with open('input/day8_input', 'r') as f:
    for line in f:
        inst = line.strip().split(' ')
        if conditions[inst[5]](inst[4], int(inst[6])):
            inc_register(inst[0], int(inst[2]) if inst[1] == 'inc' else -int(inst[2]))
            process_max = max(process_max, max(v for n, v in registers.items()))

print('Part 1: {}'.format(max(v for n, v in registers.items())))
print('Part 2: {}'.format(process_max))
