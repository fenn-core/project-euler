def fact(n):
    if n < 0 or not isinstance(n, int):
        return None
    
    if n <= 1:
        return 1 
    
    return n * fact(n-1)

val = fact(100)
print(val)
print(sum([int(i) for i in str(val)]))
