import math

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
