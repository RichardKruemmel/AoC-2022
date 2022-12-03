with open("02/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]


# Translating input into RPS logic
# 0 = Rock
# 1 = Paper
# 2 = Scissors

rps_input_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

shape_score_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

result_score_dict = {
    "W": 6,
    "D": 3,
    "L": 0,
}

# Win-lose matrix for rock, paper, scissors

rps_table = [["D", "W", "L"], ["L", "D", "W"], ["W", "L", "D"]]

score = 0

for line in lines:
    input_opponent = rps_input_dict[line[0]]
    input_me = rps_input_dict[line[2]]
    result = rps_table[input_opponent][input_me]
    score += result_score_dict[result] + shape_score_dict[line[2]]
    print(line, result)
print("Answer to Part 1:", score)
