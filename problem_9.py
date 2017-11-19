"""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

def is_pythagorean(a,b,c):
    return a**2+b**2==c**2

def generate_possible_triplets():
    possible_triplets = []
    for a in range(1,998):
        for b in range(a,998):
            c = (a**2 + b**2)**(1/2)
            if (a<b<c) and (a+b+c==1000):
                return a,b,c

a,b,c = generate_possible_triplets()
print(a*b*c)