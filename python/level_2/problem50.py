from math import sqrt, ceil


def generate_primes(top):
    vals = {num: True for num in range(2, top + 1)}
    cap = ceil(sqrt(top))

    for idx in range(2, cap + 1):
        if vals[idx]:
            for comp in range(idx * idx, top + 1, idx):
                vals[comp] = False

    ans = set()
    for num, ident in vals.items():
        if ident:
            ans.add(num)

    return ans


primes = generate_primes(1_000_000)
primes_sorted = sorted(primes)

total = sum(primes)
length = len(primes)
prefix = [0]
running = 0

for prime in primes_sorted:
    running += prime
    prefix.append(running)


longest_sum = 0
best_prime = 0

for start in range(len(primes)):
    for end in range(start + longest_sum + 1, len(prefix)):
        val = prefix[end] - prefix[start]

        if val >= 1_000_000:
            break 

        if val in primes:
            longest_sum = end - start
            best_prime = val 

print(best_prime)