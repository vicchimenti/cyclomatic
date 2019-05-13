import datetime


# function for validating user input is a valid date in the requested format
def validate_time(date_in):
    try:
        datetime.datetime.strptime(date_in, '%y-%m-%d')
    except ValueError:
        print('Invalid Date Format, enter format YY-MM-DD')
        return False
    print("You entered a valid date")
    return True


# function for gathering user input
def get_user_input():
    # Option for User Input
    date_input = input("Enter any month and day in the format YY-MM-DD: ")
    # *** IF STATEMENT ADDS 1 to Cyclomatic Complexity SCORE  ***   #
    if validate_time(date_input) is True:
        return date_input
    else:
        # Stub user input if user does not input a valid date
        date_input = stub_user_input()
        return date_input


# stub user input function
def stub_user_input():
    # return a hard-coded valid date
    return "01-01-01"


# function for generating the current timestamp
def current_timestamp():
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
    }[case]


#   ***   main driver   ***   Cyclomatic Complexity   ***   Total == 1   ***  #
# get input for switch case
case_input = str(input("Enter A, B, or C and we will convert it to an integer and print that many time stamps: "))

# Call to switch adds 1 to Cyclomatic Complexity *** Total == 2   ***   #
num_iterations = int((switch(case_input)))

#   *** FOR LOOP ADDS 1 to Cyclomatic Complexity ***   Total == 3   ***  #
for i in range(num_iterations):
    # Get Current Timestamp
    print(str(current_timestamp()))

# call get user input function adds 1 to Cyclomatic Complexity   *** Total == 4   ***   #
print(str(get_user_input()))
