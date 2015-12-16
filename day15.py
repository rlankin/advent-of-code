from functools import reduce

#ingredients = {"Butterscotch": (-1, -2, 6, 3, 8), "Cinnamon": (2, 3, -2, -1, 3)}
#ingredients = [["Butterscotch", (-1, -2, 6, 3, 8)], ["Cinnamon", (2, 3, -2, -1, 3)]]

# Read ingredients from day15_input.py
# TODO: Use regex?
ingredients = []
with open("input/day15_input.txt") as f:
    for ingredient in f:
        parsed = ingredient.rstrip().split(" ")
        #ingredients[parsed[0][:-1]] = (int(parsed[2][:-1]), int(parsed[4][:-1]), int(parsed[6][:-1]), int(parsed[8][:-1]), int(parsed[10]))
        ingredients.append([parsed[0][:-1], (int(parsed[2][:-1]), int(parsed[4][:-1]), int(parsed[6][:-1]), int(parsed[8][:-1]), int(parsed[10]))])

def get_score_1(ing, scores, tbsp):
    score = 0

    if not ing:
        if tbsp == 100 and all([True if s > 0 else False for s in scores[:-1]]):
            score = reduce(lambda x, y: x * y, scores[:-1])
    else:
        for a in range(101):
            if tbsp + a > 100:
                break

            new_scores = []
            for i, p in enumerate(ing[0][1]):
                new_scores.append(scores[i] + (p * a))

            new_score = get_score_1(ing[1:], new_scores, tbsp + a)
            if new_score > score:
                score = new_score

    return score

def get_score_2(ing, scores, tbsp):
    score = 0

    if not ing:
        if tbsp == 100 and scores[4] == 500 and all([True if s > 0 else False for s in scores[:-1]]):
            score = reduce(lambda x, y: x * y, scores[:-1])
    else:
        for a in range(101):
            if tbsp + a > 100:
                break

            new_scores = []
            for i, p in enumerate(ing[0][1]):
                new_scores.append(scores[i] + (p * a))

            new_score = get_score_2(ing[1:], new_scores, tbsp + a)
            if new_score > score:
                score = new_score

    return score

def part_1():
    score = get_score_1(ingredients, [0, 0, 0, 0, 0], 0)
    print("Part 1: " + str(score))

def part_2():
    score = get_score_2(ingredients, [0, 0, 0, 0, 0], 0)
    print("Part 2: " + str(score))

#part_1()
part_2()
