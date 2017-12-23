class Program:
    def __init__(self, pid):
        self.pid = pid
        self.registers = {'p': pid}
        self.msg_queue = []
        self.pc = 0
        self.sent_count = 0

    def assure(self, r):
        if r not in self.registers:
            self.registers[r] = 0

    def get(self, v):
        try:
            return int(v)
        except ValueError:
            self.assure(v)
            return self.registers[v]

    def set(self, v, r):
        self.assure(r)
        self.registers[r] = v

    def execute(self, inst, snd_queue):
        if inst[0] == 'jgz':
            self.pc += (self.get(inst[2]) if self.get(inst[1]) > 0 else 1)
        else:
            if inst[0] == 'snd':
                snd_queue.append(self.get(inst[1]))
                self.sent_count += 1
            elif inst[0] == 'set':
                self.set(self.get(inst[2]), inst[1])
            elif inst[0] == 'add':
                self.set(self.registers[inst[1]] + self.get(inst[2]), inst[1])
            elif inst[0] == 'mul':
                self.set(self.registers[inst[1]] * self.get(inst[2]), inst[1])
            elif inst[0] == 'mod':
                self.set(self.registers[inst[1]] % self.get(inst[2]), inst[1])
            elif inst[0] == 'rcv':
                if len(self.msg_queue) > 0:
                    self.set(self.get(self.msg_queue.pop(0)), inst[1])
                else:
                    return
            self.pc += 1

program = []
with open('input/day18_input', 'r') as f:
    program = [i.strip().split(' ') for i in f]

registers = {}

def assure(r):
    if r not in registers:
        registers[r] = 0

def get(v):
    try:
        return int(v)
    except ValueError:
        assure(v)
        return registers[v]

def part_1():
    pc = 0
    last_freq = None
    while 0 <= pc < len(program):
        inst = program[pc]
        if inst[0] == 'jgz':
            pc += (get(inst[2]) if get(inst[1]) > 0 else 1)
        else:
            if inst[0] == 'snd':
                last_freq = get(inst[1])
            elif inst[0] == 'set':
                assure(inst[1])
                registers[inst[1]] = get(inst[2])
            elif inst[0] == 'add':
                assure(inst[1])
                registers[inst[1]] += get(inst[2])
            elif inst[0] == 'mul':
                assure(inst[1])
                registers[inst[1]] *= get(inst[2])
            elif inst[0] == 'mod':
                assure(inst[1])
                registers[inst[1]] %= get(inst[2])
            elif inst[0] == 'rcv' and get(inst[1]) != 0:

                break
            pc += 1

    print('Part 1: {}'.format(last_freq))

def part_2():
    p0 = Program(0)
    p1 = Program(1)

    while 0 <= p0.pc < len(program) or 0 <= p1.pc < len(program):
        # Detect deadlock
        if (program[p0.pc][0] == 'rcv' and len(p0.msg_queue) == 0
            and program[p1.pc][0] == 'rcv' and len(p1.msg_queue) == 0):
            break

        if 0 <= p0.pc < len(program):
            p0.execute(program[p0.pc], p1.msg_queue)
        if 0 <= p1.pc < len(program):
            p1.execute(program[p1.pc], p0.msg_queue)

    print('Part 2: {}'.format(p1.sent_count))

part_1()
part_2()
