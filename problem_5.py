"""
    Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

divisors = [i for i in range(2, 21)]
print(divisors)

number = 20
reminders = [number%i for i in divisors]
while not all(reminder is 0 for reminder in reminders):
    number += 20
    reminders = [number%i for i in divisors]    
print(number)