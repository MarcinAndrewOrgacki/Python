
# dictionary. consists key value pairs. "Mary" is the key and 9.1 is the value
student_grades = {"Mary": 9.1, "Tim": 8.8, "John": 7.5}

# calculating the average grade of the students in the dictionary
mysum = sum(student_grades.values())# you use .value() to target the value in the dictionary.
length = len(student_grades)# get the number of elements in the dictionary
mean = mysum / length# divide the sum of the grades by the number of grade elements
print(mean)



