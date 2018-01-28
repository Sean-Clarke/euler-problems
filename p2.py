import math

n1 = 2
n = 3
nstore = 0
n1store = 0
sum = 2
cont = "y"

while ((n < 4000000) and (cont == "y")):
    if (n%2 == 0):
        sum += n
    nstore = n
    n += n1
    n1 = nstore
    print("sum is " + str(sum))
    print("n is " + str(n))
    print("n1 is " + str(n1))
    print("do you want to continue (y)?")
    cont = (input())
    
print(sum)
