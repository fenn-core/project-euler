from time import perf_counter
from math import sqrt, ceil


in_time = perf_counter()

def generate_primes(cap):
    candidates = {num:True for num in range(2, cap+1)}
    
    for i in range(2, ceil(sqrt(cap))+1):
        if candidates[i]:
            for j in range(i*i, cap + 1, i):
                candidates[j] = False


    vals = []
    for value, ident in candidates.items():
        if ident:
            vals.append(value)

    return vals


limit = 10_000

raw_primes = generate_primes(limit)
nums = set(i for i in range(3, limit + 2, 2))
primes = set(raw_primes)
non_prime_odds = nums.difference(primes)


for value in non_prime_odds:
    is_compliant = False
    for num in range(1, int(sqrt(value / 2)) + 1):
        if value - 2 * num * num in primes:
            is_compliant = True
            break
    
    if not is_compliant:
        print(value)
        break

final_time = perf_counter()

print(final_time-in_time)