def sentence_maker(phrase):
  interrogatives = ("how", "what", "why", "are")# words that form a question
  capitals = phrase.capitalize()# capitalizes the first letter of the input
  if phrase.startswith(interrogatives): # checks if input starts with an interrogative
    return "{}?".format(capitals)# returns the input capitalized and adds a question mark
  else:
    return "{}.".format(capitals)# returns a period at the end of the input.

results = [] # creates a list to store the phrases
while True:
  user_input = input("Say something: ") 
  if user_input == "\end": # checks if user entered the key word to end the loop
    break # ends the loop
  else:
    results.append(sentence_maker(user_input)) # calls the function and appends the user input to the list 

print(" ".join(results)) # joins the phrases together with a space in between
