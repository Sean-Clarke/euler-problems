import math

palindrome = 997899
f1 = 0
f2 = 0

pal_array = []
f2_array = []

solved = False

while solved == False:
    palindrome -= 1
    pal_array = [int(digit) for digit in str(palindrome)]
    if (len(pal_array) == 6):
        if (pal_array[0] == pal_array[5]):
            if (pal_array[1] == pal_array[4]):
                if (pal_array[2] == pal_array[3]):
                    f1 = 100
                    while f1 <= 999:
                        if ((palindrome % f1) == 0):
                            f2_array = [int(digit) for digit in str(int(palindrome / f1))]
                            if (len(f2_array) == 3):
                                print(str(palindrome / f1) + " " + str(f1))
                                solved = True
                                print(f1)
                                break
                        f1 += 1
    if (len(pal_array) == 5):
        if (pal_array[0] == pal_array[4]):
            if (pal_array[1] == pal_array[3]):
                f1 = 100
                while f1 <= 999:
                    if ((palindrome % f1) == 0):
                        f2_array = [int(digit) for digit in str(int(palindrome / f1))]
                        if (len(f2_array) == 3):
                            print(str(palindrome / f1) + " " + str(f1))
                            solved = True
                            print(f1)
                            break
                    f1 += 1

if solved == True:
    print("This is the answer: ")
    print(palindrome)
    print(f1)
else:
    print("Sorry, but this is how far I got: ")
    print(palindrome)
