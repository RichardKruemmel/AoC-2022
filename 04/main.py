assignments = []
with open("04/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]
for line in lines:
    splitted_lines = line.split(",")
    for splitted_line in splitted_lines:
        lower, upper = map(int, splitted_line.split("-"))
        assignments.append((lower, upper))

# Compare range assignments to find pairs where one fully contains the other
num_fully_contained_pairs = 0
for i in range(0, len(assignments), 2):
    a1 = assignments[i]
    a2 = assignments[i + 1]
    if a1[0] >= a2[0] and a1[1] <= a2[1]:
        num_fully_contained_pairs += 1
    elif a2[0] >= a1[0] and a2[1] <= a1[1]:
        num_fully_contained_pairs += 1

# Print the number of fully-contained pairs
print("The answer to Part One is:", num_fully_contained_pairs)

# Part two

num_overlapping_pairs = 0
for i in range(0, len(assignments), 2):
    a1 = assignments[i]
    a2 = assignments[i + 1]
    if any(val in range(a1[0], a1[1] + 1) for val in range(a2[0], a2[1] + 1)):
        num_overlapping_pairs += 1

# Print the number of overlapping pairs
print("The Answer to part two is:", num_overlapping_pairs)
