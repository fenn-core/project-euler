from time import perf_counter


initial_time = perf_counter()

total = 0
for i in range(1, 1000+1):
    total += pow(i, i)

final_time = perf_counter()


print(str(total)[-10:])
print(final_time-initial_time)