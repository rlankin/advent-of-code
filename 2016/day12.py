TEST_INPUT = ['cpy 41 a',
    'inc a',
    'inc a',
    'dec a',
    'jnz a 2',
    'dec a']

def isint(string):
    try:
        int(string)
        return True
    except:
        return False

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
                pc += int(inst[2])
                continue
        else:
            print('Unknown instruction: ' + inst[0])

        pc += 1

def part_1():
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    instructions = None

    with open('input/day12_input.txt', 'r') as f:
        instructions = [inst.strip().split() for inst in f]

    execute_assembunny(instructions, registers)

    print('Part 1: {}'.format(registers['a']))

def part_2():
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    instructions = None

    with open('input/day12_input.txt', 'r') as f:
        instructions = [inst.strip().split() for inst in f]

    execute_assembunny(instructions, registers)

    print('Part 2: {}'.format(registers['a']))

part_1()
part_2()
