import math

print("Give me a positive whole number n, and I will give you the sum of every positive whole number less than n that are also divisible by either 3, or 5!")
print("What is your n?")

ready = False;


while (ready == False):
    n = float(input())
    if ((n > 0) and (math.floor(n) % n) == 0):
        print("Thank you!")
        ready = True;
    else:
        print("Sorry, your n does not abide by the rules I have laid out for you, please give me a positive whole number!")

sum = 0

while n > 0:
    n -= 1
    if ((n%3 == 0) or (n%5 == 0)):
        sum += n

print(sum)
