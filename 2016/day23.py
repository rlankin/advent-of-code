import math

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
        else:
            print('Unknown instruction: ' + inst[0])

        # print('{} {}'.format(inst, registers))
        # input()

        pc += 1

def part_1():
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    instructions = None

    with open('input/day23_input.txt', 'r') as f:
        instructions = [inst.strip().split() for inst in f]

    execute_assembunny(instructions, registers)
    print('Part 1: {}'.format(registers['a']))

def part_2():
    # registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    # instructions = None
    #
    # with open('input/day23_input.txt', 'r') as f:
    #     instructions = [inst.strip().split() for inst in f]
    #
    # execute_assembunny(instructions, registers)

    # I arrived at this by analysis of the program.
    # input/day23_2_input.txt shows some notes I took
    print('Part 2: {}'.format(math.factorial(12) + (79 * 73)))

part_1()
part_2()
