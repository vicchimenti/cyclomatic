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
    # *** IF STATEMENT ADDS 1 to Cyclomatic Complexity
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


# mock the user input function
def mock_user_input():
    return stub_user_input()


# mock object of user input
def mock_object_user_input():
    return mock_user_input()


# function for generating the current timestamp
def current_timestamp():
    date_today = datetime.datetime.now()
    print("Current Date/Time: ")
    return date_today


#   ***   main driver   ***   #

# Get Current Timestamp and Display Before Program Action
print(str(current_timestamp()))

# call get user input function
user_input = get_user_input()

# print the mock user input
print(mock_user_input())

# print the mock object
print(mock_object_user_input())

# call validate time function
print(str(validate_time(user_input)))

# Get Updated Timestamp and Display After Program Action
print(str(current_timestamp()))
