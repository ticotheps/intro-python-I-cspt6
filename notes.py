my_list = [120, 41, 49, 92, 10]

# print all of the values in a list
for i in my_list:
    print(f"i = {i}")
print('\n')

# use the built-in 'enumerate()' method to provide indices with iterators
for (index, number) in enumerate(my_list):
    # print(f"Element at index {index} is {my_list[index]}")
    print(f"Element at index {index} is {number}")
print('\n')

# use `list comprehensions` to modify all of the items in a list WITHOUT having
# to change the items first in a `for` loop and then having to use the `.append()`
# method to add it into a new list later.

# Challenge: Create a new list containing the squares of all values in `numbers`

numbers = [1, 4, 9, 16, 25]
new_numbers = []

# `for` loop version of the Challenge
for num in numbers:
    square = num*num
    new_numbers.append(square)
print(f"new_numbers = {new_numbers}")

# `list comprehensions` version of the Challenge
squares = [ num*num for num in numbers ]
print(f"squares = {squares}")