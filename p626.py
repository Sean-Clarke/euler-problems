import math
import itertools

# A binary matrix is a matrix consisting entirely of 0s and 1s.
# Consider the following transformations that can be performed on a binary matrix:

# Swap any two rows
# Swap any two columns
# Flip all elements in a single row (1s become 0s, 0s become 1s)
# Flip all elements in a single column

# Two binary matrices A and B will be considered equivalent if
# there is a sequence of such transformations that when applied to A yields B.

# For example, the following two matrices are equivalent:

# A = ( 1 0 1 )    B = ( 0 0 0 )
#     ( 0 0 1 )        ( 1 0 0 )
#     ( 0 0 0 )        ( 0 0 1 )

# via the sequence of two transformations:
# "Flip all elements in column 3", followed by,
# "Swap rows 1 and 2".

# Define c(n) to be the maximum number of n×n binary matrices that can be found
# such that no two are equivalent.

# For example, c(3)=3.
# You are also given that c(5)=39 and c(8)=656108.

# Find c(20), and give your answer modulo 1001001011.digits?

# Personal Input:
# ---------------

# The number of unique matrix combinations made by a matrix of size n x n
# is equal to 2**n**2, eg. 16(2^2^2) for a 2x2 matrix, and 512(3^3^3) for a 3x3 matrix

# possible combinations: 2582249878086908589655919172003011874329705792829223512830659356540647622016841194629645353280137831435903171972747493376

# orbits % 1001001011 = 695577663

# orbits = 1/|G| * Summation( g.M ) for g in G
# g.M is equal to the number of m in M that g fix (ie. doesn't change)

# for a matrix of size s x s, flipping a single row or column such that the left most
# or top most and the right most or bottom most indexes are switched, has a g.M value
# of 2**s//2 (eg. 2 -> 2, 3 -> 4, 4 -> 4, 5 -> 8)

def matrix(n):
    return [[0 for i in range(0, n)] for i in range(0, n)]

def flip_row(m, r):
    for c in range(0, len(m)):
        m[r][c] ^= 1

def flip_col(m, c):
    for r in range(0, len(m)):
        m[r][c] ^= 1
        
def swap_row(m, r1, r2):
    m[r1], m[r2] = m[r2], m[r1]

def swap_col(m, c1, c2):
    for r in range(0, len(m)):
        m[r][c1], m[r][c2] = m[r][c2], m[r][c1]

def new_flip_row(m, r):
    n = []
    for i in m:
        n.append(i[:])
    for c in range(0, len(n)):
        n[r][c] ^= 1
    return n

def new_flip_col(m, c):
    n = []
    for i in m:
        n.append(i[:])
    for r in range(0, len(n)):
        n[r][c] ^= 1
    return n

def new_swap_row(m, r1, r2):
    n = []
    for i in m:
        n.append(i[:])
    n[r1], n[r2] = n[r2], n[r1]
    return n

def new_swap_col(m, c1, c2):
    n = []
    for i in m:
        n.append(i[:])
    for r in range(0, len(n)):
        n[r][c1], n[r][c2] = n[r][c2], n[r][c1]
        return n

def generate_matricies(s):
    _r = map(list, itertools.product([0, 1], repeat=s))
    _m = map(list, itertools.product([r for r in _r], repeat=s))
    print("generate_matricies has not been written yet")
    return _m

def reduce_matricies(_m):
    print("reduce_matricies has not been written yet")
    return _m

def populate_g(m):
    g = {"swap_row":[],"swap_col":[],"flip_row":[],"flip_col":[]}
    for r1 in range(0, len(m)):
        for r2 in range(r1 + 1, len(m)):
            g["swap_row"].append([r1, r2])
    for c1 in range(0, len(m)):
        for c2 in range(c1 + 1, len(m)):
            g["swap_col"].append([c1, c2])
    for r in range(0, len(m)):
        g["flip_row"].append(r)
    for c in range(0, len(m)):
        g["flip_col"].append(c)
    # len(g) = ((2 * sum(range(1, len(m))) + (2 *len(m)))
    return g

def count_g(g, matrix_size):
    "What does this function do?"
    gc = 0
    for s in range(0, matrix_size):
        print("this hasn't been written yet")
    return gc

def print_matrix(m):
    for r in m:
        print(' '.join(map(str, r)))

s = 20
c = 2**s**2
m = matrix(s)
_m = generate_matricies(s)
g = populate_g(m)

for i in g:
    print(i, g[i])
