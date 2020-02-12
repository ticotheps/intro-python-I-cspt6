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

# Challenge 1: Create a new list containing the squares of all values in `numbers`

numbers = [1, 4, 9, 16, 25]
new_numbers = []

# `for` loop version of the Challenge 1
for num in numbers:
    square = num*num
    new_numbers.append(square)
print(f"new_numbers = {new_numbers}")

# `list comprehension` version of Challenge 1
squares = [ num*num for num in numbers ]
print(f"squares = {squares}\n")

# Challenge 2: Create a new list containing only the names that start with 's'
# so that they are properly capitalized (regardless of how the name originally
# appears)

names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
print(f"names = {names}")

# `list comprehension` version of Challenge 2
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(f"s_names = {s_names}\n")

# Create an empty `dictionary` (very similar to an `object` in JavaScript)
new_dict = {}
print(f"new_dict = {new_dict}\n")

# Create a dictionary with at least two key:value pairs
food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}

# Access & print an element in the dictionary
chosen_food = 'apple'
print(food_dict[chosen_food], "\n")

# Iterate through the keys in a dictionary
for key in food_dict:
    print(f"key = {key}")
print("\n")

# Access the keys AND the values of a dictionary
for key, value in food_dict.items():
    print(f"{key} : {value}")
print("\n")
