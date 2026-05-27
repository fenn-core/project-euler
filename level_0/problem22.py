import string

letters = enumerate(string.ascii_uppercase, start=1)
values = {}
for idx, letter in letters:
    values[letter] = idx


with open("include/names.txt", "r") as names:
    raw = names.read()
    list_of_names = raw.split(",")
    for idx, name in enumerate(list_of_names):
        list_of_names[idx] = name[1:-1]

    list_of_names = sorted(list_of_names)

    sum_of_points = 0
    for idx, name in enumerate(list_of_names, start=1):
        points = 0
        for letter in name:
            points += values[letter]
        points *= idx
        sum_of_points += points

    print(sum_of_points)
