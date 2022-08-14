# USER INPUT #

def weather_conditions(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter a temperature: ")) # storing user input in a variable. you must convert input to a float because in python
                                                   # user input is taken as string.
print(weather_conditions(user_input)) # calling the function with input as a parameter
