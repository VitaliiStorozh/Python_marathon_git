# 's3ooOOooDy' has exams. He wants to study hard this time.
# He has an array of studying hours per day for the previous exams.
# He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days,
# to study as much before his current exams.
#
# Example:
#
# For a = [2,2,1,3,4,1] the answer is 3.
# [input] array.integer a
# The number of hours he studied each day.
# [output] integer
#
# The length of the maximum non-decreasing contiguous subarray.


def studying_hours(a):
    w = []
    r = 0
    x = 0
    for i in a:
        r = [1, r + 1][x <= i]
        w += [r]
        x = i
    return max(w)

print(studying_hours([2, 2, 1, 3, 4, 1]))
print(studying_hours([2, 2, 9]))
print(studying_hours([10, 100, 111, 1, 2]))
print(studying_hours(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(studying_hours(
    [1, 638, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 655, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 27, 533, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1, 835, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1,
     992]))