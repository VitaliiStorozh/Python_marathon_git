# As input data, you have a list of strings.
#
# Write a method double_string() for counting the number of strings from the list,
# represented in the form of the concatenation of two strings from this list

def double_string(s):
    return len([i for i in s if i + i in s])


data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))

data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))