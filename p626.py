import math

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

m = matrix(3)

print("")

m[0][0] = 1
m[0][1] = 1
m[0][2] = 1
m[1][1] = 1
m[2][2] = 1

for r in m:
    print(' '.join(str(n) for n in r))

print("")

swap_col(m, 0, 1)

for r in m:
    print(' '.join(str(n) for n in r))
