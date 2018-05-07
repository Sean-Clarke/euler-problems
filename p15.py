# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def grid(s):
    g = [[] for n in range(0, s)]
    for c in range(0, s):
        for r in range(0, s):
            g[c].append(0)
        g[c][0] = 1
    for c in range(0, s):
        g[0][c] ^= 1
    return g

g = grid(21)

for r in range(1, len(g)):
    for c in range(1, len(g)):
        g[r][c] = g[r-1][c] + g[r][c-1]

print(g[-1][-1])
