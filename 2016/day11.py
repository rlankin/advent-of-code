import copy

def print_floors(floors):
    for floor_num in range(len(floors) - 1, -1, -1):
        print('F{} {}'.format(floor_num, ' '.join(floors[floor_num])))

def is_valid_state(state):
    for floor in state[0]:
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
                move = copy.deepcopy(state)
                move[0][elevator_loc + d].append(item)
                move[0][elevator_loc].remove(item)
                if is_valid_state(move):
                    move[1] += d
                    move[2] += 1
                    moves.append(move)

                for item2 in state[0][elevator_loc][i + 1:]:
                    move = copy.deepcopy(state)
                    move[0][elevator_loc + d] += [item, item2]
                    move[0][elevator_loc].remove(item)
                    move[0][elevator_loc].remove(item2)
                    if is_valid_state(move):
                        move[1] += d
                        move[2] += 1
                        moves.append(move)

    return moves

def get_min_steps(state):
    state_hist = [(state[0], state[1])]
    moves = get_moves(state)

    while len(moves) > 0:
        move = moves.pop(0)

        if (move[0], move[1]) in state_hist:
            continue

        if sum([len(floor) for floor in move[0][:-1]]) == 0:
            return move[2]

        state_hist.append((move[0], move[1]))

        moves += get_moves(move)

def part_1():
    floors = [['PmG', 'PmM'],
        ['CoG', 'CmG', 'RuG', 'PuG'],
        ['CoM', 'CmM', 'RuM', 'PuM'],
        []]
    # floors = [['HM', 'LiM'],
    #     ['HG'],
    #     ['LiG'],
    #     []]

    min_steps = get_min_steps([floors, 0, 0])
    print('Part 1: {}'.format(min_steps))

part_1()
