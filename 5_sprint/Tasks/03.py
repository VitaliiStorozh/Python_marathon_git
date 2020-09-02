# Write  the function check_odd_even (number) whose input parameter is an integer number.
# The function checks whether the  set number is even or odd:
#
# in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
# in the case of an odd number the function should be displayed the corresponding message -  "Entered number is odd";
# in the case of incorrect data the function should be displayed the message - "You entered incorrect data. Please try again."
# Note: in the function you must use the "try except" construct.
#
# Function example:
#
# check_odd_even (24)     #output:    "Entered number is even"
#
# check_odd_even (19)     #output:     "Entered number is odd"

def check_odd_even(smth):
    try:
        if smth % 2:
            print("Entered number is odd")
        else:
            print("Entered number is even")
    except:
        print("You entered incorrect data. Please try again.")

check_odd_even (24)
check_odd_even (19)
check_odd_even ('retro')