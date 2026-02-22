# sum of primes below 2 million

primes = [i for i in range(3,100,2)]
primes.insert(0,2)

def isPrime(n,candidates):
    if n == 2:
        return True
    
    for i in candidates:
        if i*i > n :
            pass
        if n % i == 0:
            return False




    return True

print(isPrime(5))