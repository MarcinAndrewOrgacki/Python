# looping over a list
monday_temps = [9.1, 8.8, 7.6]
for i in monday_temps:
  
  print(round(i))

# looping over a dictionary
student_grades = {"Mary": 9.1, "Sim": 8.8, "Jim": 7.6}
for grades in student_grades.items(): # can also use .keys() and .values()
  print(grades)

phone_numbers = {"Marcin": "(647)274-9547", "Debbie": "(647)964-9540"}
for key, value in phone_numbers.items():
  print(f"{key} has a phone number {value}")

# loop and replace
client_phone = {"John K": "001234567890", "Kris B": "00123567906"}
for values in client_phone.values(): # can also use .keys() to replace the keys
  print(str.replace(values, "00", "+1"))

for values in client_phone.values():
  print(str.replace(values, "56", "99"))