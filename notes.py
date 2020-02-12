my_list = [120, 41, 49, 92, 10]

# print all of the values in a list
for i in my_list:
    print(f"i = {i}")

# use the built-in 'enumerate()' method to provide indices with iterators
for (index, number) in enumerate(my_list):
    # print(f"Element at index {index} is {my_list[index]}")
    print(f"Element at index {index} is {number}")
    
