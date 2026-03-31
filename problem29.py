nums = set()

for i in range(2, 101):
    for j in range(2, 101):
        nums.add(pow(i, j))

print(len(nums))
