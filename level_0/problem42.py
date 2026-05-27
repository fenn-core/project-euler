letter_vals = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def tri_num_generator(cap):
    vals = set()
    tri_num = 0
    num = 1
    while cap > tri_num:
        tri_num = int(0.5 * num * (num + 1))
        vals.add(tri_num)
        num += 1

    return vals


with open("include/words.txt", "r") as file:
    raw_words = file.read().split(",")
    words = []

    for word in raw_words:
        word = word.strip('"')
        words.append(word)

    count = 0
    max_val = 0
    word_vals = []
    for word in words:
        word_val = sum(letter_vals[i] for i in word)
        if word_val > max_val:
            max_val = word_val

        word_vals.append(word_val)

    tri_nums = tri_num_generator(max_val)

    for val in word_vals:
        if val in tri_nums:
            count += 1

print(count)
