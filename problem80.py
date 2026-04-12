from decimal import Decimal, getcontext


getcontext().prec = 110

p_squares = set(i*i for i in range(1, 11))

def is_perfect_square(num, perfect_squares=p_squares):
    return num in perfect_squares

total = 0

for num in range(1, 101):
    sqrt: Decimal = Decimal(num).sqrt()
    if is_perfect_square(num):
        continue

    else:
        digits = str(sqrt).replace('.', '')[:100] 
        total += sum(int(i) for i in digits)
        

print(total) 