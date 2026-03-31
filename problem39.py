def is_right_hand(a, b, c):
    return a * a + b * b == c * c


perimeter = 1000
count = 0
max_val = 0
found_val = None
while perimeter > 3:
    count = 0
    for a in range(perimeter // 3):
        for b in range(a, (perimeter - a) // 2):
            c = perimeter - a - b
            if is_right_hand(a, b, c):
                count += 1


    if count > max_val:
        max_val = count
        found_val = perimeter 

    perimeter -= 1


print(found_val)