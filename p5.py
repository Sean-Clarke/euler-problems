import math

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19]

answer = 20
solved = False

while (solved == False) and (answer <= 10000000000):
    answer += 20
    solved = True
    for n in numbers:
        if ((answer % n) != 0):
            solved = False
            break
print(answer)

# 2520 is the lowest number divisible by all the whole numbers from 1-10
# 2520 = 2 * 2 * 2 * 3 * 3 * 5 * 7
# 2^3 * 3^2 * 5 * 7

# so

# if you want to find the lowest number divisible by all the whole numbers from 1-20
# 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20
# 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

# prime factorization
