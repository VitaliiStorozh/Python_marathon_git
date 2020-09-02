# Given a string, check if its characters can be rearranged to form a palindrome.
# Where a palindrome is a string that reads the same left-to-right and right-to-left.
#
# Example
#
# "trueistrue" -> false;
# "abcab" -> true because "abcba" is a palindrome
# [input] string s (min 1 letters)
#
# [output] boolean

isPalindrome = lambda s: sum(s.count(c) % 2 for c in set(s)) < 2

print(isPalindrome("abb"))
print(isPalindrome("23332"))
print(isPalindrome("trueitrue"))
print(isPalindrome("trueistrue"))
print(isPalindrome("123123"))
print(isPalindrome("12312"))
print(isPalindrome("qqqrrr"))
print(isPalindrome("qqqrrrwww"))
print(isPalindrome("A"))