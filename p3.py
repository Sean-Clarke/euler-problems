import math

a = 600851475143

numbers = []
n = 2
count = 10000

while n < count:
    numbers.append(n)
    n += 1

prime_numbers = []

while len(numbers) > 0:
    b = numbers[0]
    prime_numbers.append(b)
    for i in numbers:
        if i % b == 0:
            numbers.remove(i)

answer = 0

while a != 1:
    if len(prime_numbers) > 0:
        if a % prime_numbers[0] == 0:
            answer = prime_numbers[0]
            print(answer)
            a = a / prime_numbers[0]
        else:
            del prime_numbers[0]

print(answer)
