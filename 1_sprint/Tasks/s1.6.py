# Write a program that given an array of integers determines
# if it is sorted in "ascending" order, "descending" order or "not sorted" at all.
#
# Example
#
# For a = [10, 5, 4], the output should be
# order(a) = "descending";
# For a = [6, 20, 160, 420], the output should be
# order(a) = "ascending";
# For a = [1, 7, 0, 4, 8, 1], the output should be
# order(a) = "not sorted".
# [input] array.integer a
#
# 1 < a.length < 100, all of numbers are different
#
# [output] string
# "ascending", "descending" or "not sorted".

def order(a):
    return "ascending" if sorted(a) == a else "descending" if sorted(a) == a[::-1] else "not sorted"


print(order([6, 20, 160, 420]))
print(order([10, 5, 4]))
print(order([1, 7, 0, 4, 8, 1]))
print(order([1, 2, 3]))
print(order(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
     90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))