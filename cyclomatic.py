# switch case function adds 1 to cyclomatic complexity total == 3
def switch(case):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'A': 4,
        'B': 5,
        'C': 6,
        'default': 10,
    }[case]


#   ***   main driver   ***   Cyclomatic Complexity   ***   Total == 1   ***  #
print("You will enter a letter which the program will use to map to a number.")
print("That number will be used to determine how many times a for loop iterates.")

# get user input for switch case
case_input = str(input("Enter A, B, or C: "))
input_validation_list = ['A', 'B', 'C', 'a', 'b', 'c']

# validate user input   ***   IF STATEMENT ADDS 1 to Cyclomatic Complexity *** Total == 2   ***   #
if case_input in input_validation_list: num_iterations = int((switch(case_input)))
else:
    # if user did not enter valid input then assign the default case
    case_input = 'default'
    num_iterations = int((switch(case_input)))

#   *** FOR LOOP ADDS 1 to Cyclomatic Complexity ***   Total == 4   ***  #
for i in range(num_iterations): print("Remaining iterations: " + str(num_iterations-(i+1)))
# This program has a cyclomatic complexity of 4 #
