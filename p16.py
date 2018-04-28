import math

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# Soltion 1 (doesn't work on extremely long integers)

# def sum_of_digits(i):
#     list_of_digits = []
#     check = 10
#     while check < i:
#         check *= 10
#     check /= 10
#     while i > 0:
#         if check > 0:
#             temp = i % check
#         else:
#             temp = 0
#         i -= temp
#         if check > 0:
#             i /= check
#         list_of_digits.append(i)
#         i = temp
#         check /= 10
#     return sum(list_of_digits)
# 
# print(sum_of_digits(2**1000))

 
def sum_of_digits(base, exp):
    n = list(str(base**exp))
    return sum([int(i) for i in n])

print(sum_of_digits(2, 1000))
