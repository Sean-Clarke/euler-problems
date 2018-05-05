import math

# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters
# used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.

def count_single(n):
    add = 0
    if (n == 9):
        add += 4
    elif (n == 8):
        add += 5
    elif (n == 7):
        add += 5
    elif (n == 6):
        add += 3
    elif (n == 5):
        add += 4
    elif (n == 4):
        add += 4
    elif (n == 3):
        add += 5
    elif (n == 2):
        add += 3
    elif (n == 1):
        add += 3
    elif (n == 0):
        print("You've asked me to count_single(0)!")
    else:
        print("You've asked me to count_single() something that isn't single digit!")
    return add
    
def count_teen(n):
    add = 0
    if (n == 19):
        add += 8
    elif (n == 18):
        add += 8
    elif (n == 17):
        add += 9
    elif (n == 16):
        add += 7
    elif (n == 15):
        add += 7
    elif (n == 14):
        add += 8
    elif (n == 13):
        add += 8
    elif (n == 12):
        add += 6
    elif (n == 11):
        add += 6
    elif (n == 10):
        add += 3
    else:
        print("You've asked me to count_teen() something that isn't between 10 and 19!")
        print(n)
    return add

def count_double(n):
    add = 0
    d = (n // 10) * 10
    r = n % 10
    if (d == 90):
        add += 6
    elif (d == 80):
        add += 6
    elif (d == 70):
        add += 7
    elif (d == 60):
        add += 5
    elif (d == 50):
        add += 5
    elif (d == 40):
        add += 5
    elif (d == 30):
        add += 6
    elif (d == 20):
        add += 6
    elif (9 < d < 20):
        print("You've asked me to count_double() something that is between 10 and 15!")
    else:
        print("You've asked me to count_double() something that isn't 2 digits!")
    if (r > 0):
        add += count_single(r)
    return add

def count_triple(n):
    add = count_single(n // 100)
    add += 7
    r = n % 100
    if (r > 0):
        add += 3
        if (r >= 20):
            add += count_double(r)
        elif ((n % 100) >= 10):
            add += count_teen(r)
        else:
            add += count_single(r)
    return add

def countem(limit):
    count = 0
    for i in range(1, limit + 1):
        if (i < 10):
            count += count_single(i)
        elif (i < 20):
            count += count_teen(i)
        elif (i < 100):
            count += count_double(i)
        elif (i < 1000):
            count += count_triple(i)
        elif (i == 1000):
            count += 11
        else:
            print("This number is greater than 1000!")
    return count

print(countem(1000))
