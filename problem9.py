from math import sqrt 
for c in range(333,500):
    for b in range(1,c):
        if 1000 == sqrt((c-b)*(c+b))+b+c :
            a = 1000 - c - b
            if a > c - b and a < b:
                print(a*b*c) 