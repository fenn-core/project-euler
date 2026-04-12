from decimal import Decimal, getcontext


getcontext().prec = 110

p_squares = set(i*i for i in range(1, int(1250**0.5)))

def is_perfect_square(num, perfect_squares=p_squares):
    return True if num in p_squares else False

total = 0

for num in range(1, 101):
    sqrt: Decimal = Decimal(num).sqrt()
    if is_perfect_square(num):
        continue

    else:
        digits = str(sqrt).split(".")
        digits = str(sqrt).replace('.', '')[:100] 
        total += sum(int(i) for i in digits)
        

print(total) 