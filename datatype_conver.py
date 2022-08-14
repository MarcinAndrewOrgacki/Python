# CONVERTING DATA TYPES #

# list to string
cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string)

# string to list
cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list)

# list to tupple
cool_list = [1, 2, 3]
cool_tuple = tuple(cool_list)
print(cool_tuple)

# tuple to list
cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list)

data = {"a": [1,2,3], "b": [4,5,6], "c": [7,8,9]}
print(data['b'][2])
