import copy

def print_floors(floors):
    for floor_num in range(len(floors) - 1, -1, -1):
        print('F{} {}'.format(floor_num, ' '.join(floors[floor_num])))

def get_moves(elevator_loc, floors):
    moves = []

    for d in [-1, 1]:
        if 0 <= elevator_loc + d < len(floors):
            for i, item in enumerate(floors[elevator_loc]):
                moves.append((d, [item]))

                for item2 in floors[elevator_loc][i + 1:]:
                    moves.append((d, [item, item2]))

    return moves

def is_valid_state(floors):
    for floor in floors:
        for item in floor:
            if item[-1] == 'M' and item[:-1] not in [i[:-1] for i in floor]:
                return False

    return True

def move(elevator_loc, floors, moves):
    if not is_valid_state(floors):
        return -1

    if sum([len(f) for f in floors[:-1]]) > 0:
        for m in get_moves(elevator_loc, floors):
            # Perform move
            new_elevator_loc = elevator_loc + m[0]
            new_floors = copy.deepcopy(floors)
            new_floors[new_elevator_loc] += m[1]
            # TODO: Is there an easier/better way to remove items like this?
            new_floors[elevator_loc] = [i for i in new_floors[elevator_loc] if i not in m[1]]

            # Continue looking for solutions
            sub_moves = move(new_elevator_loc, new_floors, moves + 1)
            if sub_moves != -1 and sub_moves < moves:
                moves = sub_moves

    return moves

def part_1():
    # floors = [['PmG', 'PmM'],
    #     ['CoG', 'CmG', 'RuG', 'PuG'],
    #     ['CoM', 'CmM', 'RuM', 'PuM'],
    #     []]
    floors = [['HM', 'LiM'],
        ['HG'],
        ['LiG'],
        []]

    min_moves = move(0, floors, -1)
    print(min_moves)
    # print(get_moves(3, floors))

part_1()
