# Numbers in the Morse code have the following pattern:
#
# all digits consist of 5 characters;
# the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
# starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
#
# Attention!
# Do not use any collection data like lists, tuples, dictionaries for holding Morse codes


def morse_number(str):
    result = ''
    for i in range(len(str)):
        if str[i] in '12345':
            result = result + '.' * int(str[i]) + '-' * (5 - int(str[i])) + ' '
        elif str[i] in '6789':
            result = result + '-' * (int(str[i]) - 5) + '.' * (10 - int(str[i])) + ' '
        else:
            result = result + '-' * 5 + ' '
    result = result[:-1]
    return (result)

print(morse_number("295"))
print(morse_number("005"))
print(morse_number("513"))
print(morse_number("784"))