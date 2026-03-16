def prime(n):
    primes = {1: 2}
    current_n = 1
    val = 3

    while current_n < n:
        is_prime = True

        for p in primes.values():
            if p*p > val:
                break
            if val % p == 0:
                is_prime = False
                break

        if is_prime:
            current_n += 1
            primes[current_n] = val

        val += 1

    return primes[n]


print(prime(10_001))