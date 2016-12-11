TARGET_LOW = 17
TARGET_HIGH = 61

look_for_target = True # There is no excuse for this. I am a bad programmer.

def get_bot(bot_num, bots):
    if bot_num not in bots:
        bots[bot_num] = {'num': bot_num, 'chips': [], 'inst': []}

    return bots[bot_num]

def get_output(output_num, outputs):
    if output_num not in outputs:
        outputs[output_num] = []

    return outputs[output_num]

def execute_bot_inst(bots_to_execute, bots, outputs):
    while len(bots_to_execute) > 0:
        bot = bots_to_execute.pop(0)
        if len(bot['chips']) == 2 and len(bot['inst']) > 0:
            if look_for_target and TARGET_LOW in bot['chips'] and TARGET_HIGH in bot['chips']:
                print('found target')
                return bot

            inst = bot['inst'].pop(0) # First instruction in queue
            low = min(bot['chips'])
            high = max(bot['chips'])

            # Give low chip
            if inst[0] == 'bot':
                get_bot(inst[1], bots)['chips'].append(low)
                bots_to_execute.append(bots[inst[1]])
            else:
                get_output(inst[1], outputs).append(low)

            # Give high chip
            if inst[2] == 'bot':
                get_bot(inst[3], bots)['chips'].append(high)
                bots_to_execute.append(bots[inst[3]])
            else:
                get_output(inst[3], outputs).append(high)

            bot['chips'].clear()

    return None

def part_1():
    bots = {} # (bot_num, [chips], [low_type, low_dest, high_type, high_dest])
    outputs = {}
    target_bot = None

    with open('input/day10_input.txt', 'r') as f:
        for inst in f:
            parsed = inst.strip().split()
            bot = None

            if parsed[0] == 'bot':
                bot = get_bot(int(parsed[1]), bots)
                bot['inst'].append([parsed[5], int(parsed[6]), parsed[10], int(parsed[11])])
            else:
                bot = get_bot(int(parsed[5]), bots)
                bot['chips'].append(int(parsed[1]))

            target_bot = execute_bot_inst([bot], bots, outputs)
            if target_bot:
                break

    print('Part 1: {}'.format(target_bot['num']))

def part_2():
    bots = {} # (bot_num, [chips], [low_type, low_dest, high_type, high_dest])
    outputs = {}

    global look_for_target
    look_for_target = False

    with open('input/day10_input.txt', 'r') as f:
        for inst in f:
            parsed = inst.strip().split()
            bot = None

            if parsed[0] == 'bot':
                bot = get_bot(int(parsed[1]), bots)
                bot['inst'].append([parsed[5], int(parsed[6]), parsed[10], int(parsed[11])])
            else:
                bot = get_bot(int(parsed[5]), bots)
                bot['chips'].append(int(parsed[1]))

            execute_bot_inst([bot], bots, outputs)

    print('Part 2: {}'.format(get_output(0, outputs)[0] * get_output(1, outputs)[0] * get_output(2, outputs)[0]))

part_1()
part_2()
