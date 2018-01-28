import math

numbers = []
n = 1
count = 100

while n <= count:
    numbers.append(n)
    n += 1

square_of_sum = 0

for i in numbers:
    square_of_sum += i

square_of_sum = square_of_sum ** 2

sum_of_squares = 0

n = 1

while n <= 100:
    sum_of_squares += n ** 2
    n += 1

if sum_of_squares >= square_of_sum:
    sum_of_squares -= square_of_sum
    print(sum_of_squares)
else:
    square_of_sum -= sum_of_squares
    print(square_of_sum)
