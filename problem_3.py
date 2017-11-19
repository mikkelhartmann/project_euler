"""
    Problem: The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 2
    600851475143 ?
"""
import numpy as np 

list_of_primes = []
for i in range(2,10000):
    reminders = [i%j for j in range(2, i)]
    if 0 not in reminders:
        list_of_primes.append(i)

prime_factors = []
target = 600851475143
for prime in list_of_primes:
    division = target/prime
    if division.is_integer():
        prime_factors.append(prime)
        target = division
        print(prime, target)