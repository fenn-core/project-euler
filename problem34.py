def fact(n, cache=None):
    if cache is None:
        cache = {}

    if n <= 1:
        return 1 

    if n in cache:
        return cache[n]
    
    cache[n] = n * fact(n-1, cache)

    return cache[n]

facts = {}
for idx in range(10): 
    facts[idx] = fact(idx)

maxval = 7 * facts[9]

vals = []
num = 10
for num in range(10, maxval):
    total = 0
    num_str = str(num)
    for i in num_str:
        total += facts[int(i)]
    if total == num:
        vals.append(num)

print(sum(vals))