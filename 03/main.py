with open("03/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

characters = "abcdefghijklmnopqrstuvwxyz"
sum = 0
for line in lines:
    length = round(len(line) / 2)
    first_compartement = line[:length]
    second_compartement = line[length:]
    common_characters = list(set(first_compartement) & set(second_compartement))

    for character in common_characters:
        # check if character is lower case
        if character in characters:
            # find index of character in characters
            index = characters.index(character)
            sum += index + 1
        else:
            lower_case_character = character.lower()
            index = characters.index(lower_case_character)
            sum += index + 27

print("The answer to Part 1 is:", sum)

sum = 0
for number in range(0, len(lines), 3):
    first_group = lines[number]
    second_group = lines[number + 1]
    third_group = lines[number + 2]
    common_characters = list(set(first_group) & set(second_group) & set(third_group))
    for character in common_characters:
        # check if character is lower case
        if character in characters:
            # find index of character in characters
            index = characters.index(character)
            sum += index + 1
        else:
            lower_case_character = character.lower()
            index = characters.index(lower_case_character)
            sum += index + 27
print(sum)
