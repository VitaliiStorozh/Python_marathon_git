# Nicky and Dev work in a company where each member is given his income in the form of points.
# On Nicky's birthday, Dev decided to give some of his points as a gift.
# The number of points Dev is gifting is the total number of visible zeros visible
# in the string representation of the N points he received this month.
#
# Let's say that Nicky got M points from Dev. By the company law, if M is even and greater than 0,
# Nicky must give one point to the company. If M is odd, the company gives Nicky one additional point.
#
# Given the number of points N Dev received this month, calculate the number of points
# Nicky will receive as a gift and return this number in its binary form.
#
# Note: visible zeros are calculated as follows:
#
# 0, 6 and 9 contain 1 visible zero each;
# 8 contains 2 visible zeros;
# other digits do not contain visible zeros.
# Example
#
# For N = "565", the output should be
# Cipher_Zeroes(N) = 10.
#
# There's one visible zero in "565". Since one is odd, the company will give an additional point, so Nicky will receive 2 points.
# 210 = 102, so the output should be 10.
#
# Input/Output
#
# [input] string N
#
# The number of points Dev received this month.
#
# Constraints:
# 1 ≤ N ≤ 101000.
#
# [output] integer
#
# The number of points Nicky will receive in the binary representation.


def Cipher_Zeroes(N):
    t = N.count
    t = t("6") + t("0") + t("9") + 2 * t("8")
    t += [-1, 1][t % 2]
    return int(bin([0, t][t>0])[2:])


def Cipher_Zeroes(N):
    point = 0
    for digit in N:
        if digit == '0' or digit == '6' or digit == '9':
            point += 1
        elif digit == '8':
            point += 2

    if point % 2 == 0 and point > 0:
        point -= 1
    elif point > 0:
        point += 1
    point_str = str(bin(point))
    point = int(point_str[2:])
    return (point)

print(Cipher_Zeroes("565"))
print(Cipher_Zeroes("8200"))
print(Cipher_Zeroes("4900"))
print(Cipher_Zeroes("7481"))
print(Cipher_Zeroes("4"))
print(Cipher_Zeroes("0"))
print(Cipher_Zeroes("2628426728"))