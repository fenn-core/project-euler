vals = []
for num in range(1, 1_000_000):
    num_str = str(num)
    if num_str[::-1] == num_str:
        bin_str  = bin(num)[2:]
        if bin_str == bin_str[::-1]:
            vals.append(num)

print(vals)
print(sum(vals))