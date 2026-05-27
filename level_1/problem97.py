import sys
from time import perf_counter

initial_time = perf_counter()

sys.set_int_max_str_digits(2_400_000)

val = 28433 * pow(2, 7830457) + 1

final_time = perf_counter()


print(final_time-initial_time)

print(str(val)[-10:])