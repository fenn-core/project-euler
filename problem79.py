with open("keylog.txt", "r") as keylog:
    nums = keylog.read().split("\n")

nums.remove("")
used = set()
passcode = ""

for num in nums:
    for i in num:
        used.add(i)

strs = [j for j in used]
sets = [set() for k in range(len(strs))]
after = dict(zip(strs, sets))

for num in nums:
    after[num[0]].add(num[1])
    after[num[0]].add(num[2])
    after[num[1]].add(num[2])


n = 0

for _ in range(len(after.keys())):
    for key, val in after.items():
        if len(val) - n == 0:
            passcode += key
            n += 1 
    
    
print(passcode[::-1])
