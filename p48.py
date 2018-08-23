# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# 
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

c = 1
i = 2

while i <= 1000:
	c += i**i
	i+=1
