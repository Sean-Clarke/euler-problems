import math

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

answer = 2
add = True

for n in range(3, 2000000, 2):
    add = True
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            add = False
            break
    if add == True:
        answer += n
        print(n)

print(answer)
