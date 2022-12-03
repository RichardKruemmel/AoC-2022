with open("01/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

# Grouping the lines
groups = []
group = []
for line in lines:
    if line == "":
        groups.append(group)
        group = []
    else:
        group.append(int(line))
# Part 1
largest_sum = 0
for group in groups:
    if sum(group) > largest_sum:
        largest_sum = sum(group)
print("Answer to Part 1:", largest_sum)

# Part 2
summed_groups = [sum(group) for group in groups]
summed_groups.sort(reverse=True)

print("Answer to Part 2:", summed_groups[0] + summed_groups[1] + summed_groups[2])
