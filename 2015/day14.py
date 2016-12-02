RACE_DURATION = 2503
reindeer = {}

with open("input/day14_input.txt") as f:
    for r in f:
        parsed = r.rstrip().split(" ")
        reindeer[parsed[0]] = (int(parsed[3]), int(parsed[6]), int(parsed[13]))

def part_1():
    distances = {}

    for r, s in reindeer.items():
        time_remaining = RACE_DURATION
        distance = 0

        while time_remaining > 0:
            if s[1] <= time_remaining:
                distance += s[0] * s[1]
            time_remaining -= s[1] + s[2]

        distances[r] = distance

    print("Part 1: " + str(max([d for r, d in distances.items()])))

def part_2():
    r_stats = {}
    for r, s in reindeer.items():
        r_stats[r] = [0, 0, s[1], 0] # Score, Distance, Time to Fly, Time to Rest

    lead = 0
    for i in range(RACE_DURATION):
        for r, s in reindeer.items():
            if r_stats[r][2] > 0:
                # If the reindeer has time left to fly, then move it further
                r_stats[r][1] += s[0]
                r_stats[r][2] -= 1

                # If the reindeer has no more time to fly, begin resting
                if r_stats[r][2] == 0:
                    r_stats[r][3] = s[2]
            elif r_stats[r][3] > 0:
                # If the reindeer is resting, decrement TTR
                r_stats[r][3] -= 1

                # If the reindeer is done resting, reset its TTF
                if r_stats[r][3] == 0:
                    r_stats[r][2] = s[1]

            # Update the running total of the lead position
            if r_stats[r][1] > lead:
                lead = r_stats[r][1]

        # Score points
        for r, s in r_stats.items():
            if s[1] == lead:
                s[0] += 1

    print("Part 2: " + str(max([s[0] for r, s in r_stats.items()])))

part_1()
part_2()
