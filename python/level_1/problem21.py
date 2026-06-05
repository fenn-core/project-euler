def proper_divisor_sum(num):
    total = 0
    for divisor in range(1, num//2 + 1):
        if not (num % divisor):
            total += divisor

    return total


vals = []
for idx in range(1, 10_000):
    total = proper_divisor_sum(idx)
    if total != idx and proper_divisor_sum(total) == idx:
        vals.append(total)

print(sum(vals))
