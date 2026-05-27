n = 2
a = 1
b = 1 
while True:
    if len(str(b)) >= 1000:
        print(n)
        break
    a, b = b, a + b
    n += 1