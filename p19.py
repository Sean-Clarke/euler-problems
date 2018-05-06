# This question was worded very poorly, so I have rewritten it...

# January 1 1901 was a Tuesday and is the first day of the 20th century.
# December 31 2000 was the last day of the 20th century.

# April, June, September, and November all have thirty days.
# February has twenty-eight days, except on leap years, when it has twenty-nine.
# Every other month has thirty-one days.

# Every non-century year evenly divisible by 4 (1904, 1908, 1912...)
# is considered a leap year, as well as centuries divisible by 400 (2000).

# How many Sundays fell on the first of the month throughout the twentieth century?

import math

def leap_year(year):
    if (year % 4 == 0):
        return 29
    else:
        return 28

def next_day(day, month, year):
    months = {0: 31, 1: leap_year(year), 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
    nday = day + months[month]
    nday %= 7
    return nday

def next_month(month):
    nmonth = month + 1
    if (nmonth == 12):
        nmonth = 0
    return nmonth

sundays = 0
cyear = 1901
cmonth = 0
cday = 2
lyear = 2000

while (cyear <= lyear):
    if (cday == 0):
        sundays += 1
    cday = next_day(cday, cmonth, cyear)
    cmonth = next_month(cmonth)
    if (cmonth == 0):
        cyear += 1
print(sundays)
    
    
