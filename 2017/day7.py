class TreeNode:
    name = ''
    weight = 0
    total_weight = None
    parent = None
    children = []

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def get_total_weight(self):
        if self.total_weight is None:
            self.total_weight = self.weight + sum(c.get_total_weight() for c in self.children)
        return self.total_weight

def find_unbalanced_program(program):
    if len(program.children) == 0:
        return

    for c in program.children:
        p = find_unbalanced_program(c)
        if p is not None:
            return p

    if not all(c.get_total_weight() == program.children[0].get_total_weight() for c in program.children):
        return program

programs = {}
with open('input/day7_input', 'r') as f:
    for line in f:
        program = line.strip().split(' ')
        children = [] if len(program) <= 2 else [c.replace(',', '') for c in program[3:]]
        programs[program[0]] = TreeNode(program[0], int(program[1][1:-1]), children)
    for n, p in programs.items():
        child_nodes = []
        for child in p.children:
            child_nodes.append(programs[child])
            programs[child].parent = p
        p.children = child_nodes

bottom = next(p for n, p in programs.items() if p.parent is None)

print('Part 1: {}'.format(bottom.name))

print('Part 2:')
unbalanced = find_unbalanced_program(bottom)
for c in unbalanced.children:
    print('{} ({}) -- {}'.format(c.name, c.weight, c.get_total_weight()))
