numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)


product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)
