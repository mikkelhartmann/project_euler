"""
    Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
"""

list_of_primes = [2, 3]
for i in range(3,100000000, 2):
    reminders = [i%prime for prime in list_of_primes]
    if 0 not in reminders:
        list_of_primes.append(i)
    if len(list_of_primes)==10001:
        print(list_of_primes[-1])
        break