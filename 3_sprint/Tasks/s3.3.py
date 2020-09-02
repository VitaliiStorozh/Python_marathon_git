# Create function create_account(user_name: string, password: string, secret_words: list).
# This function should return inner function check.
#
# The function check compares the values of its arguments with password and secret_words:
# the password must match completely, secret_words may be misspelled (just one element).
#
# Password should contain at least 6 symbols including one uppercase letter,
# one lowercase letter,  special character and one number.
#
# Otherwise function create_account raises ValueError.


import re
import copy

def create_account(str0, str1, list):
    user_name = str0
    pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*[$%!#*^_].*)[0-9a-zA-Z$%!#*^_]{6,}$')
    if pattern_password.match(str1):
        password = str1
    else:
        raise ValueError
    secret_words = list
    def check(str2, list1):
        if str2 == str1:
            list2 = copy.deepcopy(list1)
            if len(list2) == len(list):
                list_test = []
                for item in list:
                    if item in list2:
                        list2.remove(item)
                    else:
                        list_test.append(item)
                if len(list2) == 0:
                    return True
                if len(list2) == len(list_test) and len(list2) == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return check

