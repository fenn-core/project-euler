from time import perf_counter


initial_time = perf_counter()

def fact(n):
    if 1 >= n:
        return 1
    
    return fact(n-1) * n

facts = list(fact(i) for i in range(101))


def n_choose_r(n, r, facts=facts):
    numerator = 1 
    
    for idx in range(r):
        numerator *= (n - idx)

    return numerator // facts[r]


count = 0
for i in range(1, 101):
    for j in range(1, i+1):
        if  n_choose_r(i, j) > 1_000_000:
            count += 1 

print(count)

final_time = perf_counter()

print(final_time-initial_time)