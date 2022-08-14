# mean(ave) function
def mean(mylist): # using mylist as a parameter
    the_mean = sum(mylist) / (len(mylist)) # the sum of mylist(1+4+5) divided by the length of mylist(3 items) 10 / 3
    return the_mean 

print(mean([1, 4, 5])) # printing the function call.

# currency converter
def convert(amount): # amount is the input currency
    output = amount * 1.75 # 1.75 is the coefficient
    return output

print(convert(10))    

