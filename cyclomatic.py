import datetime


# function for generating the current timestamp
def current_timestamp():
    print("Printing the Current Time Stamp: ")
    date_today = datetime.datetime.now()
    print("Current Date/Time: ")
    return date_today


# switch case function
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
print("Each time the loop iterates it will print a current time stamp.")
input_validation_list = ['A', 'B', 'C', 'a', 'b', 'c']
# get user input for switch case
case_input = str(input("Enter A, B, or C: "))

# validate user input with   ***   IF STATEMENT ADDS 1 to Cyclomatic Complexity *** Total == 2   ***   #
if case_input in input_validation_list:
    # Call to switch adds 1 to Cyclomatic Complexity *** Total == 3   ***   #
    num_iterations = int((switch(case_input)))
else:
    # if user did not enter valid input then assign the default case
    case_input = 'default'
    # Call to switch adds 1 to Cyclomatic Complexity *** Total == 3   ***   #
    num_iterations = int((switch(case_input)))

#   *** FOR LOOP ADDS 1 to Cyclomatic Complexity ***   Total == 4   ***  #
for i in range(num_iterations): print(str(current_timestamp()))
