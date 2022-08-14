# append function. adds to list
monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(12.4)
print(monday_temperatures)# [9.1, 8.8, 7.5, 12.4]
monday_temperatures.remove(12.4)
print(monday_temperatures)

# clear function. clears the list of all items
monday_temperatures.clear()
print(monday_temperatures)# []

# index function. tells you the index of the item
monday_temperature = [9.1, 9.9, 4.2]
print(monday_temperature)
print(monday_temperature.index(4.2))

# get item from index
monday_temperature[2]
print(monday_temperature[2])

# UPPER LIMIT IS ALWAYS EXCLUSIVE #
# accessing list slices
print(monday_temperature[0:2])# first num is starting index, second is ending index exclusive. you can omit the 0 [:2]
print(monday_temperature[1:])# will print from index 1 to end, 1 is inclusive.

# negative indexing. start at the end of the list and count in. starts at -1.
print(monday_temperature[-1])
print(monday_temperature[-2:])# will print last 2 items
