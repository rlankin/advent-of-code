def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def toggle(inst):
    if inst[0] == 'inc':
        inst[0] = 'dec'
    elif inst[0] in ('dec', 'tgl'):
        inst[0] = 'inc'
    elif inst[0] == 'jnz':
        inst[0] = 'cpy'
    elif inst[0] == 'cpy':
        inst[0] = 'jnz'

def execute_assembunny(instructions, registers):
    output = None
    output_counter = 0

    pc = 0
    while pc < len(instructions):
        inst = instructions[pc]
        if inst[0] == 'cpy':
            registers[inst[2]] = int(inst[1]) if isint(inst[1]) else registers[inst[1]]
        elif inst[0] == 'inc':
            registers[inst[1]] += 1
        elif inst[0] == 'dec':
            registers[inst[1]] -= 1
        elif inst[0] == 'jnz':
            value = int(inst[1]) if isint(inst[1]) else registers[inst[1]]
            if value != 0:
                pc += int(inst[2]) if isint(inst[2]) else registers[inst[2]]
                continue
        elif inst[0] == 'tgl':
            i = pc + (int(inst[1]) if isint(inst[1]) else registers[inst[1]])
            if 0 <= i < len(instructions):
                toggle(instructions[i])
        elif inst[0] == 'out':
            value = int(inst[1]) if isint(inst[1]) else registers[inst[1]]
            if value not in (0, 1) or value == output:
                return False
            else:
                output = value
                output_counter += 1
        else:
            print('Unknown instruction: ' + inst[0])

        if output_counter == 1000:
            return True

        pc += 1

def part_1():
    a = 0
    registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    instructions = None

    with open('input/day25_input.txt', 'r') as f:
        instructions = [line.strip().split() for line in f]

    while not execute_assembunny(instructions, registers):
        a += 1
        registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
        print('Trying a = {}'.format(registers['a']))

    print('Part 1: {}'.format(a))

part_1()
