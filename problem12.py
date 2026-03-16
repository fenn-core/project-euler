from math import sqrt, floor 


def triangle_num(n):
    return (n*(n+1)//2)

maxval = 0
maxnum = 0
n = 1
while maxval < 501:
    n += 1 
    triangle_number = triangle_num(n)
    division_cap = floor(sqrt(triangle_number))
    divisors = 0
    for divisor in range(1,division_cap+1):
        if triangle_number % divisor == 0:
            if triangle_number // divisor == 1:
                divisors += 1 
            else:
                divisors += 2
                
    if maxval < divisors:
        maxval = divisors
        maxnum = triangle_number
    

print(maxnum)