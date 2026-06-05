hs = {} 
def fib(n):
    if n == 1 or n ==0:
        return 1
    
    if n in hs:
        return hs[n]
    
    hs[n] = fib(n-1) + fib(n-2)
    return hs[n]
    

n, total = 1, 0
while fib(n) < 4e6:
    fib_num = fib(n)
    if fib_num % 2 == 0:
        total += fib_num
    n += 1

print(total)
