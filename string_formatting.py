# STRING FORMATTING

userInput = input("Enter your name: ")
message = "Hello %s!" % userInput # you must use this version if python version is lower than 3.6
print(message)

            # OR #

user_input = input("Enter your name: ")
message = f"Hello {user_input}" # can you this version is python version is 3.6 and above
print(message)

# 2 VARIABLES

name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
hey = "Hope"
b = "all"
c = "is well"

#####################################################################

message = "Hello %s %s " % (name, last_name)
print(message)
message2 = f"Hello {name} {last_name}. {hey} {b} {c}"
print(message2)

######################################################################

name = "John"
surname = "Smith"
message3 = "Your name is {}. Your surname is {}".format(name, surname)
print(message3)

