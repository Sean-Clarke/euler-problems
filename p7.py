import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

n = 2
add = False

prime_numbers = [2]

while len(prime_numbers) < 10001:
    for i in prime_numbers:
        add = True
        if n % i == 0:
            add = False
            break
    if add == True:
        prime_numbers.append(n)
    n += 1

print(prime_numbers[10000])
