mult_3 = {i for i in range(3,1000,3)}
mult_5 = {i for i in range(5,1000,5)}

print(sum(mult_3.union(mult_5)))