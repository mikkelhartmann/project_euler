"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def proper_divisors_of(n):
    proper_divisors = []
    for num in range(1, n):
        if (n%num == 0):
            proper_divisors.append(num)
    return proper_divisors

print("proper divisors of 200", proper_divisors_of(200))
print("Their sum is", sum(proper_divisors_of(200)))
print("proper divisors of 284", proper_divisors_of(284))
print("Their sum is", sum(proper_divisors_of(284)))

amicable_numbers = set()
for a in range(0, 10000):
    b = sum(proper_divisors_of(a))
    d_of_b = sum(proper_divisors_of(b))
    if (a == d_of_b) & (a != b):
        amicable_numbers.add(a)
        amicable_numbers.add(b)
        

print(sum(amicable_numbers))