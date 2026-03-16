def fact(n, cache=None):
    if cache is None:
        cache = {}

    if n <= 1:
        return 1 

    if n in cache:
        return cache[n]
    
    cache[n] = n * fact(n-1)

    return cache[n]

vals = []
num = 10
while True:
    total = 0
    num_str = str(num)
    for i in num_str:
        total += fact(int(i))
    if total == num:
        vals.append(num)
    num += 1 
    print(sum(vals))