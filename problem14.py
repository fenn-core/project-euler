def collatz(n):
    if n <= 1:
        return [n]
    vals = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            vals.append(n)
        else:
            n = 3 * n + 1
            vals.append(n)
    return vals

maxval = 0
max_n = 2  
for n in range(2,1_000_000):
    vals =  collatz(n)
    length = len(vals)
    if maxval < length:
        maxval = length
        max_n = n

print(maxval)
print(max_n)