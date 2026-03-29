from math import sqrt


def is_pentagonal(n):
    return not ((1+sqrt(1+24*n)) % 6)

def pentagonal_num(n):
    return (n*(3*n-1) // 2)

# considering the growth of pentagonal numbers, to reach the 
# minimized value we should pick the first number that complies

not_found = True
i = 1
sum_val, diff_val = 0, 0

while not_found:
    for j in range(1, i):
        sum_val = pentagonal_num(i) + pentagonal_num(j)
        diff_val = pentagonal_num(i) - pentagonal_num(j)

        if is_pentagonal(sum_val) and is_pentagonal(diff_val):
            print(diff_val)
            not_found = False
            break 

    i += 1
    