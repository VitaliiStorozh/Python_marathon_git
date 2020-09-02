# Given number n and two permutations p and q of length n. Find a permutation r,
# such that for every 1 <= i <= n, q[i] = p[r[i]].
#
# Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.
#
# Example
#
# Input:
# n = 3, p = [3, 1, 2],  q = [2, 1, 3]
#
# Output:
# r = [3, 2, 1]
# [input] integer n
#
# length of the permutations
#
# [input] array.integer p
## [input] array.integer q
## [output] array.integer
## permutation r

findPermutation = lambda n, p, q: [p.index(i) + 1 for i in q]

n = 5
p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]
print(findPermutation(n, p, q))

n = 3
p = [3, 1, 2]
q = [2, 1, 3]
print(findPermutation(n, p, q))

n = 10
p = [8, 5, 4, 1, 10, 6, 9, 2, 7, 3]
q = [7, 6, 10, 5, 1, 8, 9, 3, 2, 4]
print(findPermutation(n, p, q))

n = 100
p = [45, 62, 36, 89, 31, 4, 48, 94, 35, 43, 10, 68, 65, 34, 100, 21, 93, 52, 98, 49, 20, 39, 2, 81, 32, 71, 11, 87, 33,
     66, 51, 23, 55, 42, 63, 57, 72, 86, 80, 18, 54, 14, 44, 69, 95, 30, 50, 37, 25, 64, 96, 15, 90, 99, 8, 28, 12, 76,
     61, 9, 67, 6, 78, 7, 17, 46, 5, 26, 24, 97, 75, 1, 70, 41, 16, 53, 59, 84, 19, 47, 74, 73, 85, 79, 88, 77, 60, 83,
     58, 38, 29, 27, 91, 82, 56, 13, 40, 3, 92, 22]
q = [91, 12, 35, 33, 13, 24, 22, 63, 27, 58, 56, 54, 88, 23, 14, 67, 50, 17, 25, 48, 2, 8, 97, 3, 90, 60, 52, 53, 65,
     10, 9, 61, 38, 19, 32, 28, 26, 51, 98, 71, 76, 80, 79, 89, 93, 81, 39, 18, 4, 45, 5, 83, 41, 36, 70, 31, 6, 1, 15,
     99, 30, 74, 29, 16, 34, 100, 68, 59, 49, 86, 20, 85, 69, 42, 40, 47, 78, 62, 64, 82, 96, 92, 11, 57, 37, 66, 55,
     87, 72, 77, 21, 43, 95, 7, 75, 84, 46, 94, 73, 44]
print(findPermutation(n, p, q))