# largest palindromic product
largest = 0
for i in range(100,1000):
    for j in range(i,1000):
        s = str(i * j)
        if s == s[::-1] and i*j > largest:
            largest = i*j

print(largest)