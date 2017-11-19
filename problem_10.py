"""
    Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

limit = 2000000 #2000000

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        # start with 1
        primes.append(p)
        # remove all multiples of p 
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(limit)
print(sum(primes))