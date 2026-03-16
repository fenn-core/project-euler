


def prime_generator(cap):
    primes = [2]
    current_number = 3
    while current_number < cap:
        is_prime = True
        for prime in primes:
            if prime*prime > current_number:
                break

            if current_number % prime == 0:
                is_prime = False
                current_number += 2
                break

        
        if is_prime:
            primes.append(current_number)
            current_number += 2

    return primes

print(sum(prime_generator(2_000_000)))