from time import perf_counter


initial_time = perf_counter()

vals = set()

for a in range(1, 100):
    for b in range(1, 100):
        vals.add(pow(a, b))

max_sum = 0
current_sum = 0

for num in vals:
    for element in str(num):
        current_sum += int(element)
    if current_sum > max_sum:
        max_sum = current_sum
    current_sum = 0

print(max_sum)

final_time = perf_counter()

print(final_time - initial_time)
