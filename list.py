from statistics import mean


student_grades = [9.1, 8.8, 7.5, 8.8] #list
student_marks = [91, 89, [33, 45, 67]] #list in a list

#creating a list in a range of numbers
student_grade = list(range(0, 11)) #creates a list of numbers from 0 to 10 [0,1,2,3,4,5,6,7,8,9,10]

student_grade = list(range(0, 11, 3)) #includes a step, move across the list by a step of 2. [0,2,4,6,8,10] by 3 [0,3,6,9]
print(student_grade)

# BUILT-IN FUCTIONS. USE THE FUNCTIONS ON THE ITEM THAT YOU NEED TO PERFORM THE FUNCTION ON #

# get the mean(average) of a list
mysum = sum(student_grades) #sum is a bulit-in function that add items together
length = len(student_grades) #len is a built-in function that counts number of elements
mean = mysum / length # you a dividing the sum of added numbers by the count of elements in the list. so 25.4 / 3
print(mean)

# get max value of a list. use dir(__builtins__) to see all available builtin functions
max_value = max(student_grades)
print(max_value)

# will print how many 8.8 there are in the list
print(student_grades.count(8.8))