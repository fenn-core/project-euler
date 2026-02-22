rng = range(1,101)

sum_of_squares = sum([(i**2) for i in rng])
square_of_sum = sum([i for i in rng])**2
print(square_of_sum - sum_of_squares)