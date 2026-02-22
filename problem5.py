# smallest number evenly divisible by 1, 2, 3, ... 20

from math import factorial as fact
divisors = [i for i in range(2,20)]

num = fact(20)
for i in divisors:
    while num % i == 0:
        num //= i
    num * i 

print(num)