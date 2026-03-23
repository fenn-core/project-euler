primes = {2, 3, 5, 7}

def prime_generator(start, stop):
    num = start if (start % 2) else start + 1 

    while stop > num:
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break

            if not (num % prime):
                is_prime = False 
                break 
            
        if is_prime:
            primes.add(num)
        
        num += 2    


previous_level = 9
buffer_low = 3 # skip 2 and previous non-primes
buffer_high = 1000
not_found = True

while not_found:
    prime_generator(buffer_low, buffer_high)
    for num in range(previous_level, buffer_high+1, 2):
        if num in primes:
            continue
        
        is_compliant = False
        for val in range(1, int((num / 2) ** 0.5)+1):
            if (num - 2 * val * val) in primes:
                is_compliant = True
                break
    
        if not is_compliant:
            print(num)
            not_found = False
            break
        
            
    buffer_low = buffer_high + 1 
    buffer_high += 1000