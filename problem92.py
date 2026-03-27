def square_chain(num):
    loops_1 = {44, 32, 13, 10, 1}
    loops_89 = {85, 145, 42, 20, 4, 16, 37, 58, 89}

    
    while True:
        if num in loops_1:
            return 1
        if num in loops_89:
            return 89

        num = sum(int(i)**2 for i in str(num))

ans = 0
ans_check = 0
for num in range(1, 10_000_000):
    val = square_chain(num)
    if val == 89:
        ans += 1
    if val == 1:
        ans_check += 1
     

print(ans)
print((ans+ans_check) == (10_000_000-1))