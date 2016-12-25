import copy

def print_floors(floors):
    for floor_num in range(len(floors) - 1, -1, -1):
        print('F{} {}'.format(floor_num, ' '.join(floors[floor_num])))

def is_valid_state(floors):
    for floor in floors:
        for item in floor:
            if item[-1] == 'M' and item[:-1] + 'G' not in floor \
                and len([i for i in floor if i[-1] == 'G']) > 0:
                return False

    return True

def get_moves(state):
    moves = []
    elevator_loc = state[1]

    for d in [-1, 1]:
        if 0 <= elevator_loc + d < len(state[0]):
            for i, item in enumerate(state[0][elevator_loc]):
                move = [list(f) for f in state[0]]
                # print('Converted move: {}'.format(move))
                # print('from state[0]: {}'.format(state[0]))
                move[elevator_loc + d].append(item)
                move[elevator_loc].remove(item)
                if is_valid_state(move):
                    moves.append((tuple(tuple(f,) for f in move), state[1] + d, state[2] + 1))

                for item2 in state[0][elevator_loc][i + 1:]:
                    move = [list(f) for f in state[0]]
                    # print('Converted move: {}'.format(move))
                    # print('from state[0]: {}'.format(state[0]))
                    move[elevator_loc + d] += [item, item2]
                    move[elevator_loc].remove(item)
                    move[elevator_loc].remove(item2)
                    if is_valid_state(move):
                        moves.append((tuple(tuple(f,) for f in move), state[1] + d, state[2] + 1))

    return moves

def get_min_steps(state):
    state_hist = {(state[0], state[1])}
    moves = get_moves(state)

    while len(moves) > 0:
        move = moves.pop(0)

        # print('Move: {}'.format(move))
        # print('State hist:')
        # for h in state_hist:
        #     print('  {}'.format(h))
        # input()

        if (move[0], move[1]) in state_hist:
            continue

        if sum([len(floor) for floor in move[0][:-1]]) == 0:
            return move[2]

        state_hist.add((move[0], move[1]))

        moves += get_moves(move)

def part_1():
    floors = (('PmG', 'PmM'),
        ('CoG', 'CmG', 'RuG', 'PuG'),
        ('CoM', 'CmM', 'RuM', 'PuM'),
        ())
    # floors = (('HM', 'LiM'),
    #     ('HG',),
    #     ('LiG',),
    #     ())

    min_steps = get_min_steps((floors, 0, 0))
    print('Part 1: {}'.format(min_steps))

part_1()
