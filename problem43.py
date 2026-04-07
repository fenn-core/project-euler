from time import perf_counter

initial_time = perf_counter()

vals = []
digits = [str(i) for i in range(10)]

def remove_dupes(arr):
    return [x for x in arr if len(set(x)) == len(x)]

def extend_suffixes(sfx1, sfx2, divisor):
    for element in sfx1:
        for digit in digits:
            if digit not in element:
                window = digit + element[:2]
                if int(window) % divisor == 0:
                    sfx2.append(digit + element)


suffixes_17 = [f"{i:03d}" for i in range(17, 1000, 17)]
suffixes_17 = remove_dupes(suffixes_17)

suffixes_13 = []
suffixes_11 = []
suffixes_7 = []
suffixes_5 = []
suffixes_3 = []
suffixes_2 = []


extend_suffixes(suffixes_17, suffixes_13, 13)
extend_suffixes(suffixes_13, suffixes_11, 11)
extend_suffixes(suffixes_11, suffixes_7, 7)
extend_suffixes(suffixes_7, suffixes_5, 5)
extend_suffixes(suffixes_5, suffixes_3, 3)
extend_suffixes(suffixes_3, suffixes_2, 2)

total = 0

for num in suffixes_2:
    for digit in digits:
        if digit not in num:
            final_num = digit + num
            total += int(final_num)

print(total)

final_time = perf_counter()

print(final_time - initial_time)