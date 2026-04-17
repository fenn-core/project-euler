from math import log10
from time import perf_counter


initial_time = perf_counter()

with open("base_exp.txt", "r") as file:
    values = []
    raw_txt = file.read().split("\n")
    for element in raw_txt:
        values.append(element.split(","))

max_val = 0
max_base = 0

for base, exponent in values:
    base, exponent = int(base), int(exponent)
    val = exponent * log10(base)
    if val > max_val:
        max_val = val
        max_base = base

for value in values:
    if value[0] == str(max_base):
        idx = values.index(value) + 1

print(idx)

final_time = perf_counter()

print(final_time - initial_time)
