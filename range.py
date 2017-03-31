for value in range(1,6):
    print(value)
# use list function to make an array(list)

numbers = list(range(1,6))
print(numbers)
even_numbers =list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,11):
    square= value**2
    squares.append(square)

print squares
# list comprehensions combine multiple steps into one?

squares2 = [value**2 for value in range(1,11)]
print(squares2)
