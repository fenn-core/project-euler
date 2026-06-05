def prime_generator(n):
    primes = {1:2}
    if n <= 1 or not isinstance(n, int):
        return primes

    val = 3
    idx = 2
   
    while idx <= n:
        is_prime = True
        for prime in primes.values():
            if prime*prime > val:
                break
            
            if val % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes[idx] = val
            idx += 1  
        
        val += 2
        
    return primes


def trun_check():
    max_prime = 750
    vals = set()
    while len(vals) < 11:
        primes = prime_generator(max_prime)
        primes_set = set(primes.values())
        for prime in primes_set:
            trun = True
            prime_str = str(prime)
            for idx in range(1, len(prime_str)):
                if int(prime_str[:idx]) not in primes_set:
                    trun = False
                    break
                if int(prime_str[idx:]) not in primes_set:
                    trun = False
                    break

            if trun:
                if prime > 9:
                    vals.add(prime)
        
        max_prime += 750

    return sorted(vals)
    
        
values = trun_check()
print(values)
print(sum(values))