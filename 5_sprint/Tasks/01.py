# Write  the function check_day_week(day) whose input parameter is a number. The function returns the
# corresponding day of the week if the input parameter is in the range of 1 to 7, namely
#
# · in the case when the input parameter is 5 the function should be displayed the message – "Friday"
# · in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message
# – "There is no such day of the week!Please try again."
# · in the case of incorrect data the function should be displayed the message\
#                                                                      - "You did not enter a number!Please try again."
#
# Note: in the function you must use the "try except" construct.
#
# Function example:
#
# check_day_week(2)                       # output:   "Tuesday"
#
# check_day_week(11)                     # output:  "There is no such day of the week!Please try again."
#
# check_day_week("Monday")       # output:   "You did not enter a number!Please try again."
#


def check_day_week(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        if 0<day<8:
            print(days[day-1])
        else:
            print(days[9])
    except IndexError:
        print("There is no such day of the week!Please try again.")
    except TypeError:
        print("You did not enter a number!Please try again.")

check_day_week(2)
check_day_week(11)
check_day_week("monday")