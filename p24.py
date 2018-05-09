# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.

# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

def make_p(_digits):
    _p = 1
    p_count = 2

    while p_count <= _digits:
        _p *= p_count
        p_count += 1

    return _p

def lex_perm_of(p, _d):
    _p = make_p(len(_d))
    answer = []

    while len(_d) > 0:
        f = _p / len(_d)
        i = math.ceil(p * len(_d) / _p) - 1
        answer.append(_d.pop(i))
        _p = f
        f *= i
        p -= f

    return answer

print(lex_perm_of(1000000, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
