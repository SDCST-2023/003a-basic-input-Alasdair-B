#! python3

# this line uses the input command to 
# display some text, and then waits for a response
# note that the statement includes a variable assignment with the entry
# stored into the variable "data"
# the contents of the parentheses are displayed as output
data = input("Please enter some data and then press the Enter Key")


# the entry is displayed back to the user but prefixed with 
# a description and the + operator that joins 2 strings together
print("You entered:" + data)

print("\n\n\n\n\n\n\n\n")

# in this example, the question to be asked is stored in a variable
# so the input statement only has to display the variable, instead of
# the string literal
question = "How are you feeling today?"
response = input(question)
print(f"I am happy to hear that you are feeling {response}")
