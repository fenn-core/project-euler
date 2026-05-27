from math import ceil, sqrt
from time import perf_counter

first_time = perf_counter()

def generate_primes(top):
    vals = {num: True for num in range(2, top + 1)}
    cap = ceil(sqrt(top))

    for idx in range(2, cap + 1):
        if vals[idx]:
            for comp in range(idx * idx, top + 1, idx):
                vals[comp] = False

    ans = []
    for num, ident in vals.items():
        if ident:
            ans.append(num)

    return ans


b_vals = []
raw_primes = generate_primes(1_000_000)

for prime in raw_primes: 
    if prime > 1000:
        break 
    b_vals.append(prime)

primes = set(raw_primes)


max_count = 0
max_product = 1
max_a = 0 

for a in range(-999, 1000):
    for b in b_vals:
        n = 0
        value = b
        while value in primes:
            n += 1 
            value = n*n + a*n + b
            n += 1 

        if n > max_count:
            max_count = n
            max_product = a * b 
            max_a = a

last_time = perf_counter()

print(max_count, max_product)
print(max_a, max_product//max_a)
print(last_time-first_time)