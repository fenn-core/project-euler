from math import sqrt


def is_pent_num(num):
    val = (1+sqrt(1+24*num))/6
    return val.is_integer()

count = 0
n = 1
while 3 > count:
    hex_num = n * (2*n-1)
    if is_pent_num(hex_num):
        count += 1 
        print(hex_num) 

    n += 1 

