"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import numpy as np

def proper_divisors_of(n):
    nums = np.arange(1, n)
    reminders = n%nums
    proper_divisors = nums[np.where(reminders==0)]
    return proper_divisors

def create_all_sums_of_abundant_numbers(abundant_numbers):
    sum_of_abundant_numbers = set()
    for a in abundant_numbers:
        for b in abundant_numbers:
            sum_of_abundant_numbers.add(a+b)
    return sum_of_abundant_numbers

abundant_numbers = []
for number in range(1, 28123):
    if number < sum(proper_divisors_of(number)):
        abundant_numbers.append(number)

sum_of_abundant_numbers = create_all_sums_of_abundant_numbers(abundant_numbers)

not_sum_of_two_abundant_number = []
for number in range(1, 28123):
    if number not in sum_of_abundant_numbers:
        not_sum_of_two_abundant_number.append(number)

print(not_sum_of_two_abundant_number)
print(sum(not_sum_of_two_abundant_number))