def prime_generator(cap):
    if cap < 2:
        return set()
    
    cache = [2]
    current_number = 3

    while current_number <= cap:
        is_prime = True

        for prime in cache:
            if prime * prime > current_number:
                break
            if current_number % prime == 0:
                is_prime = False
                break

        if is_prime:
            cache.append(current_number)

        current_number += 2

    return cache

primes = set(prime_generator(1_000_000))


def circle_num(num):
    vals = set()
    num_str = str(num)
    length = len(num_str)
    for idx in range(length):
        circ_num = num_str[idx:] + num_str[:idx]
        vals.add(int(circ_num))
    return vals


forbidden_nums = set(["0", "2", "4", "6", "5", "8"])
seen = set()
vals = {2, 3, 5, 7} 

for num in range(3, 1_000_000, 2):
    if num in seen:
        continue

    str_num = str(num)
    if any(d in str_num for d in forbidden_nums):
        continue

    circle_numbers = circle_num(num)

    all_are_prime = True
    for circle_number in circle_numbers:
        if circle_number not in primes:
            all_are_prime = False
            break

    seen.update(circle_numbers)

    if all_are_prime:
        vals.update(circle_numbers)

print(vals)
print(len(vals))