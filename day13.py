people = {}

with open("input/day13_input.txt") as f:
    for relation in f:
        parsed = relation.rstrip().split(" ")
        person = parsed[0]
        other = parsed[10][:-1]

        if person not in people:
            people[person] = {}
        people[person][other] = int(parsed[3]) if parsed[2] == "gain" else -int(parsed[3])

def get_net_happiness(happiness, curr, unseated, h_totals, first):
    if not unseated and curr != first:
        h_totals.add(happiness + people[curr][first] + people[first][curr])

    for person in unseated:
        if person != curr:
            net = happiness + people[curr][person] + people[person][curr]
            get_net_happiness(net, person, [p for p in unseated if p != person], h_totals, first)

def part_1():
    unseated = [person for person in people]
    h_totals = set()
    for person in unseated:
        get_net_happiness(0, person, [p for p in unseated if p != person], h_totals, person)

    print("Part 1: " + str(max(h_totals)))

def part_2():
    people["Ryan"] = {}
    for person in people:
        if person != "Ryan":
            people["Ryan"][person] = 0
            people[person]["Ryan"] = 0

    unseated = [person for person in people]
    h_totals = set()
    for person in unseated:
        get_net_happiness(0, person, [p for p in unseated if p != person], h_totals, person)

    print("Part 2: " + str(max(h_totals)))

part_1()
part_2()
