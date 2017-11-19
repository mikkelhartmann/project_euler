"""
    Problem: A palindromic number reads the same both ways. The largest palindrome made from
    the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(number):
    size = len(str(number))
    halfway = int(size/2)
    start = str(number)[:halfway]
    end = str(number)[halfway:]
    if start == end[::-1]:
        return True
    else:
        return False

def product(number_one, number_two):
    return number_one*number_two

def get_number_pairs():
    pairs = []
    for i in range(1,999):
        for j in range(1,999):
            pair = (i,j)
            pairs.append(pair)
    return pairs

pairs = get_number_pairs()
solution = 0

for pair in pairs:
    prod = product(pair[0], pair[1])
    if is_palindrome(prod) and prod>solution:
        solution = prod
        print(pair, prod)