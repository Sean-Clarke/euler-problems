# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the properdivisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

import math

def get_divisors(n):
    m = int(math.sqrt(n))
    d = [1]

    if (m**2 == n):
        d.append(m)
    else:
        m += 1
    for i in range(2, m):
        if n % i == 0:
            d.append(i)
            d.append(n / i)
    return d

def is_excessive(n):
    if n >= 12:
        return sum(get_divisors(n)) > n
    else:
        return False

def is_sum_of_excessives(n):
    for i in _e:
        if i > n:
            return False
        if (n - i) in soe:
            return True
    return False

_e = [n for n in range(1, 28123 + 1) if is_excessive(n)]
soe = set(_e)
answer = sum(n for n in range(1, 28123 + 1) if not is_sum_of_excessives(n))

print(answer)
