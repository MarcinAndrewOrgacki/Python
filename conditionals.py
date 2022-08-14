# if statement on a list or dictionary
def mean(value):
    if type(value) == dict: # checking if the input value is of type dictionary
      the_mean = sum(value.values()) / len(value) # if so, it is adding all values(9.1+8.8+7.5) and 
    else:                                         # dividing them by the number of values(3) in dictionary
      the_mean = sum(value) / len(value) # if not, it's adding the values and dividing by number of values in a list

    return the_mean

student_grades = {"Mary": 9.1, "Tim": 8.8, "John": 7.5} # dictionary
print(mean(student_grades))

# elif conditional
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")