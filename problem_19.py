"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

month_to_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Create isLeapYear function
def isLeapYear(year):
    return (( year%4==0 ) & (year%400 == 0) )

# Initialize the counter
counter = 0

# For each year from 1991 to 2000
days_since_januar_1_1900 = 365
for year in range(1901, 2001):
    print(year)

    if isLeapYear(year):
        month_to_day[1] = 29
    else:
        month_to_day[1] = 28
    
    for days_in_month in month_to_day:
        days_since_januar_1_1900 += days_in_month
        if days_since_januar_1_1900%7 == 6:
            print("The day was a sunday!")
            counter += 1
print(counter)

print("The answer is", counter==171)