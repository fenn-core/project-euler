from math import sqrt, ceil


def generate_primes(top):
    vals = {num: True for num in range(2, top + 1)}
    cap = ceil(sqrt(top))

    for idx in range(2, cap + 1):
        if vals[idx]:
            for comp in range(idx * idx, top + 1, idx):
                vals[comp] = False

    lst = []
    for num, ident in vals.items():
        if ident:
            lst.append(num)

    return lst


def is_pandigital(num):
    num_str = str(num)
    length = len(num_str)
    seen = set()
    for letter in num_str:
        idx = int(letter)
        if not idx:
            return False
        if idx > length:
            return False
        if idx in seen:
            return False
        
        seen.add(idx)

    if len(seen) != length:
        return False
    
    return True


def tri_nums():
    return [n*(n+1)//2 for n in range(1, 10)]

print(tri_nums())
# reject 21, 321, 54321, 654321, 87654321, 987654321 

primes = generate_primes(7654321)[::-1]

for prime in primes:
    if is_pandigital(prime):
        print(prime)
        break