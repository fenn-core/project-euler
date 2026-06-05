# 600851475143
# largest prime factor 

val = 600851475143
largest = 0
while val % 2 == 0 :
    largest = 2 
    n //= 2

factor = 3 
while factor **2 < val:
    while val % factor == 0:
        largest = factor 
        val //= factor 
    factor += 2 

if val > 1 :
    print(val)
else: 
    print(largest)