from math import sqrt, floor

def divcheck(n):
    divcap = 20
    divnum = 2
    while divnum <= divcap:
        if n % divnum != 0:
            return False
        divnum += 1
    
    return True

flag = True
n = 2
while flag:
    n += 1 
    flag = not(divcheck(n))
print(n)