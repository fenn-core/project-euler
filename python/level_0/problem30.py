max_val = 0 

n = "9"
while True:
    n += "9"
    if int(n) >= ((9**5) * len(n)):
        break
    

cap_val = int(n)
vals = []

for num in range(2, cap_val):
    if num == sum([int(i)**5 for i in str(num)]):
        vals.append(num)

print(vals)
print(sum(vals))